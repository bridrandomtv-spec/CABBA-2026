import { Router, Request, Response, NextFunction } from 'express';
import bcrypt from 'bcryptjs';
import jwt from 'jsonwebtoken';
import { query } from './db/index.js';

export const authRouter = Router();

const JWT_SECRET = process.env.SESSION_SECRET || 'fallback-secret-do-not-use-in-prod';

export interface AuthUser {
  id: string;
  email: string;
  displayName: string;
  avatarUrl: string | null;
  role: string;
  createdAt: Date;
}

// Extend Express Request to include user
declare global {
  namespace Express {
    interface Request {
      user?: AuthUser;
    }
  }
}

// Middleware to extract and verify JWT
export const requireAuth = (req: Request, res: Response, next: NextFunction): void => {
  const token = req.cookies?.session;
  
  if (!token) {
    res.status(401).json({ error: 'Unauthorized' });
    return;
  }

  try {
    const decoded = jwt.verify(token, JWT_SECRET) as AuthUser;
    req.user = decoded;
    next();
  } catch (error) {
    res.status(401).json({ error: 'Invalid or expired session' });
  }
};

export const requireAdmin = (req: Request, res: Response, next: NextFunction): void => {
  if (req.user?.role !== 'admin') {
    res.status(403).json({ error: 'Forbidden: Admins only' });
    return;
  }
  next();
};

const setSessionCookie = (res: Response, user: AuthUser) => {
  const token = jwt.sign(user, JWT_SECRET, { expiresIn: '7d' });
  res.cookie('session', token, {
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    sameSite: 'lax',
    maxAge: 7 * 24 * 60 * 60 * 1000 // 7 days
  });
};

authRouter.post('/register', async (req: Request, res: Response): Promise<void> => {
  try {
    const { email, password, displayName } = req.body;

    if (!email || !password || !displayName) {
      res.status(400).json({ error: 'Missing required fields' });
      return;
    }

    // Check if email is already in use
    const existingUser = await query('SELECT id FROM users WHERE email = $1', [email]);
    if (existingUser.rows.length > 0) {
      res.status(409).json({ error: 'Email already in use' });
      return;
    }

    const passwordHash = await bcrypt.hash(password, 10);

    const result = await query(
      `INSERT INTO users (email, password_hash, display_name, role)
       VALUES ($1, $2, $3, 'user')
       RETURNING id, email, display_name, avatar_url, role, created_at`,
      [email, passwordHash, displayName]
    );

    const userRow = result.rows[0];
    const user: AuthUser = {
      id: userRow.id,
      email: userRow.email,
      displayName: userRow.display_name,
      avatarUrl: userRow.avatar_url,
      role: userRow.role,
      createdAt: userRow.created_at
    };

    setSessionCookie(res, user);
    res.status(201).json({ user });
  } catch (error) {
    console.error('Register error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

authRouter.post('/login', async (req: Request, res: Response): Promise<void> => {
  try {
    const { email, password } = req.body;

    if (!email || !password) {
      res.status(400).json({ error: 'Missing credentials' });
      return;
    }

    const result = await query(
      'SELECT id, email, password_hash, display_name, avatar_url, role, created_at FROM users WHERE email = $1',
      [email]
    );

    if (result.rows.length === 0) {
      res.status(401).json({ error: 'Invalid credentials' });
      return;
    }

    const userRow = result.rows[0];
    const isMatch = await bcrypt.compare(password, userRow.password_hash);

    if (!isMatch) {
      res.status(401).json({ error: 'Invalid credentials' });
      return;
    }

    const user: AuthUser = {
      id: userRow.id,
      email: userRow.email,
      displayName: userRow.display_name,
      avatarUrl: userRow.avatar_url,
      role: userRow.role,
      createdAt: userRow.created_at
    };

    setSessionCookie(res, user);
    res.json({ user });
  } catch (error) {
    console.error('Login error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

authRouter.post('/logout', (req: Request, res: Response) => {
  res.clearCookie('session');
  res.json({ success: true });
});

authRouter.get('/me', requireAuth, (req: Request, res: Response) => {
  res.json({ user: req.user });
});

// Used when updating profile
authRouter.patch('/profile', requireAuth, async (req: Request, res: Response): Promise<void> => {
  try {
    const { displayName, avatarUrl } = req.body;
    const userId = req.user!.id;
    
    let updateQuery = 'UPDATE users SET updated_at = NOW()';
    const params: any[] = [];
    let paramIndex = 1;

    if (displayName) {
      updateQuery += `, display_name = $${paramIndex++}`;
      params.push(displayName);
    }
    
    if (avatarUrl !== undefined) {
      updateQuery += `, avatar_url = $${paramIndex++}`;
      params.push(avatarUrl);
    }

    updateQuery += ` WHERE id = $${paramIndex} RETURNING id, email, display_name, avatar_url, role, created_at`;
    params.push(userId);

    const result = await query(updateQuery, params);
    if (result.rows.length === 0) {
      res.status(404).json({ error: 'User not found' });
      return;
    }

    const userRow = result.rows[0];
    const user: AuthUser = {
      id: userRow.id,
      email: userRow.email,
      displayName: userRow.display_name,
      avatarUrl: userRow.avatar_url,
      role: userRow.role,
      createdAt: userRow.created_at
    };

    // Refresh the session with new data
    setSessionCookie(res, user);
    res.json({ user });
  } catch (error) {
    console.error('Update profile error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});
