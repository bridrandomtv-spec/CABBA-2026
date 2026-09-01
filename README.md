# شباب أهلي برج بوعريريج - المنصة الرقمية

هذا المشروع هو تجسيد للمنصة الرقمية الرسمية لنادي CABBA، مصمم ليكون منصة متكاملة وطويلة المدى لربط النادي بجمهوره العريض في الداخل والخارج.

## الميزات الرئيسية:
- **الرئيسية**: آخر الأخبار والمباريات القادمة.
- **مركز المباريات**: تغطية حية، إحصائيات، التشكيلة، واختيار رجل المباراة.
- **CABBA TV**: مكتبة الأغاني والأهازيج (مع كلمات الأغاني) وملخصات الفيديو.
- **المتجر والتذاكر**: شراء منتجات النادي الرسمية وتذاكر المباريات.
- **العضوية والملف الشخصي**: بطاقة الانخراط الرقمية (QR)، نقاط الولاء، ولعبة التوقعات.
- **المساعد الذكي**: مساعد يعتمد على Gemini AI للإجابة على استفسارات الأنصار.

---

# Documentation technique

Application React 19 + Vite 6 + Tailwind 4, servie par un serveur Express qui
expose aussi le point d'entrée Gemini. Interface en arabe, mise en page RTL,
pensée mobile d'abord et installable comme PWA.

## Démarrage

```bash
npm install
cp .env.example .env      # puis renseigner GEMINI_API_KEY
npm run dev               # http://localhost:3000
```

Le serveur de développement monte Vite en mode middleware : une seule commande
sert le front et l'API, sans problème de CORS.

## Scripts

| Script | Rôle |
| --- | --- |
| `npm run dev` | Serveur de développement (Express + Vite middleware) |
| `npm run build` | Build du front dans `dist/` + bundle du serveur en `dist/server.cjs` |
| `npm start` | Lance le build de production (nécessite `NODE_ENV=production`) |
| `npm run lint` / `npm run typecheck` | Vérification TypeScript (`tsc --noEmit`) |
| `npm run tidy` | Archive dans `scripts/legacy/` les scripts de génération de la racine, ainsi que les anciens `manifest.json` et `sw.js` désormais remplacés par ceux de `public/` |

## Structure

```
index.html            Point d'entrée, métadonnées PWA et sociales
server.ts             Express : POST /api/chat (Gemini), GET /api/health, statiques
public/               Servi tel quel et copié dans dist/ au build
  manifest.json       Manifeste PWA
  sw.js               Service worker
  icon.svg            Icône vectorielle (source des PNG)
src/
  main.tsx            Montage React, ErrorBoundary, enregistrement du SW
  App.tsx             Coquille : en-tête, navigation, panneau assistant
  types.ts            Types partagés (Tab, ChatMessage, Product…)
  ThemeContext.tsx    Thème sombre/clair
  index.css           Tailwind, utilitaires safe-area, variables du thème clair
  lib/storage.ts      Accès localStorage centralisé et tolérant aux erreurs
  hooks/              useFavorites, useNotificationSettings
  components/         34 écrans et composants
scripts/
  generate-icons.html Génère icon-192.png et icon-512.png
  tidy-root.mjs       Rangement de la racine
```

## Icônes PWA

Le manifeste attend `public/icon-192.png` et `public/icon-512.png`, absents du
dépôt. Ouvre `scripts/generate-icons.html` dans un navigateur, clique sur le
bouton, puis dépose les deux fichiers dans `public/`. Si tu obtiens le logo
officiel du club, remplace-les en conservant les mêmes noms et dimensions.

## Thème clair

Plutôt que de conditionner chaque composant, `.theme-light` (posé sur `<html>`)
redéfinit les variables de couleur de Tailwind dans `src/index.css` : les classes
`bg-zinc-900`, `text-white`, `bg-black` s'inversent d'elles-mêmes. En ajoutant
une nuance de gris à un composant, vérifie qu'elle est bien déclarée dans le bloc
`.theme-light`, sinon elle restera sombre en mode clair.

## Service worker

`public/sw.js` applique « réseau d'abord » à la navigation, `stale-while-revalidate`
aux fichiers statiques, et ne met jamais `/api/` en cache. Incrémente
`CACHE_VERSION` à chaque déploiement qui modifie l'app shell. Le worker n'est
enregistré qu'en production (`import.meta.env.PROD`) pour ne pas gêner le
rechargement à chaud.

## Données et limites actuelles

Les contenus (matchs, joueurs, produits, sondages, commentaires live) sont des
données de démonstration codées en dur dans les composants. `MATCHES_DATA` est
exporté depuis `components/MatchCalendar.tsx` et réutilisé par `Profile.tsx`.

Points restants à traiter, par ordre d'utilité :

1. **Notifications réelles.** `MatchAlert` simule une alerte toutes les 60 s à
   partir des préférences. Un vrai système demande la Push API, un abonnement
   `pushManager.subscribe()`, un stockage côté serveur et un déclencheur.
2. **Source de données.** Extraire les données de démonstration des composants
   vers un module ou une API, pour que les écrans cessent de dupliquer les mêmes
   listes.
3. **Historique de l'assistant.** Le contexte est renvoyé à chaque requête et
   borné à 20 tours ; il n'est pas persisté entre deux ouvertures du panneau.
4. **Tests.** Aucun test pour l'instant. `lib/storage.ts` et
   `hooks/useNotificationSettings.ts` (migration du schéma) sont les premiers
   candidats.
5. **Fichiers de verrouillage.** `bun.lock` et `package-lock.json` coexistent :
   garder celui du gestionnaire réellement utilisé.
