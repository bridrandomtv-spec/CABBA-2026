import pg from 'pg';
import dotenv from 'dotenv';
dotenv.config();

const pool = new pg.Pool({ connectionString: process.env.DATABASE_URL });
pool.query('SELECT NOW()')
  .then(res => { console.log('PG CONNECTED:', res.rows[0]); process.exit(0); })
  .catch(err => { console.error('PG ERROR:', err.message); process.exit(1); });
