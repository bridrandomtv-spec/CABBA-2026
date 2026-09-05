const fs = require('fs');
let code = fs.readFileSync('server/db/migrations/001_init_auth.sql', 'utf-8');
if (!code.includes('pgcrypto')) {
  code = "CREATE EXTENSION IF NOT EXISTS pgcrypto;\n\n" + code;
  fs.writeFileSync('server/db/migrations/001_init_auth.sql', code);
}
