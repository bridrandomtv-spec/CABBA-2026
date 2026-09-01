export type Tab = 'home' | 'match' | 'chants' | 'tv' | 'store' | 'profile' | 'community';

export interface ChatMessage {
  id: string;
  role: 'user' | 'ai';
  text: string;
  timestamp: Date;
}

export interface NewsItem {
  id: string;
  title: string;
  excerpt: string;
  date: string;
  imageUrl?: string;
}

export interface MediaItem {
  id: string;
  title: string;
  duration: string;
  type: 'audio' | 'video';
  thumbnailUrl?: string;
  lyrics?: string;
}

export interface Product {
  id: string;
  name: string;
  price: number;
  imageUrl: string;
  category: 'kit' | 'merch';
}
