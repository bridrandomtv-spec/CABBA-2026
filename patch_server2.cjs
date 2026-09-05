const fs = require('fs');
let code = fs.readFileSync('server.ts', 'utf-8');
code = code.replace(
  'import { authRouter } from "./server/auth";',
  'import { authRouter } from "./server/auth.ts";'
);
fs.writeFileSync('server.ts', code);
