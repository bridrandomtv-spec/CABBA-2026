import express from "express";
import path from "path";
import { GoogleGenAI } from "@google/genai";
import dotenv from "dotenv";

dotenv.config();

const app = express();
// Cloud Run (et la plupart des hébergeurs) imposent le port via la variable
// d'environnement PORT. Le 3000 codé en dur empêchait tout démarrage en ligne.
const PORT = Number(process.env.PORT) || 3000;
const HOST = "0.0.0.0";

const GEMINI_API_KEY = process.env.GEMINI_API_KEY;

if (!GEMINI_API_KEY) {
  // Sans cette vérification, l'absence de clé produisait une erreur 500 opaque
  // au premier message envoyé, sans indication de la cause.
  console.warn(
    "[CABBA] GEMINI_API_KEY absente : l'assistant renverra une erreur. " +
      "Copiez .env.example vers .env et renseignez la clé.",
  );
}

app.use(express.json({ limit: "128kb" }));

const ai = new GoogleGenAI({ apiKey: GEMINI_API_KEY ?? "" });

const SYSTEM_INSTRUCTION = `أنت مساعد ذكي مخصص لأنصار نادي شباب أهلي برج بوعريريج (CABBA).
تتحدث باللغة العربية بطلاقة، ويمكنك التحدث باللهجة الجزائرية إذا لزم الأمر.
مهمتك هي مساعدة الأنصار في كتابة منشورات لدعم الفريق، اقتراح شعارات (Slogans)، وتوليد أفكار لمساندة النادي في أزمته المالية والرياضية.
ألوان الفريق هي الأصفر والأسود (الجراد الأصفر). كن دائمًا إيجابيًا وحماسيًا!`;

/** Nombre maximal de tours conservés, pour borner la taille du contexte envoyé. */
const MAX_HISTORY_TURNS = 20;

interface ClientMessage {
  role?: unknown;
  text?: unknown;
}

/**
 * Convertit l'historique du client vers le format attendu par le SDK Gemini.
 *
 * L'ancienne version parcourait `history` dans une boucle vide : l'assistant
 * repartait donc de zéro à chaque message et ne pouvait pas suivre une
 * conversation ("et lui ?", "reformule", etc.).
 */
function toGeminiHistory(history: unknown) {
  if (!Array.isArray(history)) return [];

  return history
    .filter((entry): entry is ClientMessage => typeof entry === "object" && entry !== null)
    .filter((entry) => typeof entry.text === "string" && (entry.text as string).trim().length > 0)
    .map((entry) => ({
      // Le SDK attend "model" là où le client utilise "ai".
      role: entry.role === "user" ? ("user" as const) : ("model" as const),
      parts: [{ text: entry.text as string }],
    }))
    .slice(-MAX_HISTORY_TURNS);
}

app.post("/api/chat", async (req, res) => {
  try {
    const { message, history } = req.body ?? {};

    // On envoie puis on sort, sans `return res.…` : les types d'Express 5
    // attendent `void | Promise<void>` et refusent un handler qui renvoie `res`.
    if (typeof message !== "string" || !message.trim()) {
      res.status(400).json({ error: "Message is required" });
      return;
    }

    if (!GEMINI_API_KEY) {
      res.status(503).json({ error: "خدمة المساعد غير مهيأة حالياً." });
      return;
    }

    const chat = ai.chats.create({
      model: "gemini-2.5-flash",
      history: toGeminiHistory(history),
      config: {
        systemInstruction: SYSTEM_INSTRUCTION,
        temperature: 0.7,
      },
    });

    const response = await chat.sendMessage({ message });

    res.json({ text: response.text });
  } catch (error) {
    console.error("Error calling Gemini API:", error);
    res.status(500).json({ error: "فشل في الاتصال بالذكاء الاصطناعي." });
  }
});

// Sonde de disponibilité, utile pour l'hébergeur et pour vérifier la config.
app.get("/api/health", (_req, res) => {
  res.json({ status: "ok", geminiConfigured: Boolean(GEMINI_API_KEY) });
});

async function startServer() {
  if (process.env.NODE_ENV !== "production") {
    // Import dynamique : avec un import statique, esbuild produit un `require("vite")`
    // en tête de dist/server.cjs, ce qui obligeait à installer Vite (un outil de
    // build) sur le serveur de production, y compris avec `npm ci --omit=dev`.
    const { createServer as createViteServer } = await import("vite");
    const vite = await createViteServer({
      server: { middlewareMode: true },
      appType: "spa",
    });
    app.use(vite.middlewares);
  } else {
    const distPath = path.join(process.cwd(), "dist");
    app.use(express.static(distPath));
    app.get("*all", (_req, res) => {
      res.sendFile(path.join(distPath, "index.html"));
    });
  }

  app.listen(PORT, HOST, () => {
    console.log(`Server running on http://localhost:${PORT}`);
  });
}

startServer().catch((error) => {
  // Une erreur ici (port occupé, Vite qui ne démarre pas) restait silencieuse :
  // le processus se terminait sans message.
  console.error("[CABBA] impossible de démarrer le serveur :", error);
  process.exit(1);
});
