const fs = require('fs');
let code = fs.readFileSync('server.ts', 'utf-8');
code = code.replace(
  'import dotenv from "dotenv";',
  'import dotenv from "dotenv";\nimport cookieParser from "cookie-parser";\nimport { authRouter } from "./server/auth.js";'
);
code = code.replace(
  'app.use(express.json({ limit: "128kb" }));',
  'app.use(express.json({ limit: "128kb" }));\napp.use(cookieParser());\napp.use("/api/auth", authRouter);'
);
fs.writeFileSync('server.ts', code);
