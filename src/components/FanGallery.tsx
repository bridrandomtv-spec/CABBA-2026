import { useState } from 'react';
import { Camera, Heart, MessageCircle } from 'lucide-react';

interface FanPost {
  id: string;
  author: string;
  avatar: string;
  image: string;
  caption: string;
  upvotes: number;
  comments: number;
  time: string;
}

const initialPosts: FanPost[] = [
  {
    id: '1',
    author: 'أمين برايجي',
    avatar: 'A',
    image: 'https://images.unsplash.com/photo-1614632537190-23e4146777db?auto=format&fit=crop&q=80&w=400&h=400',
    caption: 'أجواء رائعة في الملعب اليوم، الفوز إن شاء الله! 🟡⚫',
    upvotes: 124,
    comments: 12,
    time: 'منذ ساعتين'
  },
  {
    id: '2',
    author: 'يوسف العاصمة',
    avatar: 'Y',
    image: 'https://images.unsplash.com/photo-1522778119026-d647f0596c20?auto=format&fit=crop&q=80&w=400&h=400',
    caption: 'الجراد الأصفر دائماً في الموعد.. لن تسير وحدك أبداً يا أهلي',
    upvotes: 89,
    comments: 5,
    time: 'منذ 4 ساعات'
  }
];

export default function FanGallery() {
  const [posts, setPosts] = useState<FanPost[]>(initialPosts);
  const [upvotedPosts, setUpvotedPosts] = useState<Record<string, boolean>>({});

  const handleUpvote = (postId: string) => {
    setPosts(prev => prev.map(post => {
      if (post.id === postId) {
        const isUpvoted = upvotedPosts[postId];
        return {
          ...post,
          upvotes: isUpvoted ? post.upvotes - 1 : post.upvotes + 1
        };
      }
      return post;
    }));
    setUpvotedPosts(prev => ({
      ...prev,
      [postId]: !prev[postId]
    }));
  };

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between mb-2 mt-4">
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 rounded-full bg-yellow-500/10 flex items-center justify-center text-yellow-500">
            <Camera size={16} />
          </div>
          <h3 className="font-bold text-white text-lg">عدسة الجماهير</h3>
        </div>
      </div>

      <div className="space-y-4">
        {posts.map(post => {
          const isUpvoted = upvotedPosts[post.id];
          return (
            <div key={post.id} className="bg-zinc-900 border border-zinc-800 rounded-2xl overflow-hidden shadow-sm">
              <div className="p-3 flex items-center justify-between border-b border-zinc-800/50">
                <div className="flex items-center gap-2">
                  <div className="w-8 h-8 rounded-full bg-zinc-800 border border-zinc-700 flex items-center justify-center text-xs font-bold text-white">
                    {post.avatar}
                  </div>
                  <div>
                    <h4 className="font-bold text-white text-xs">{post.author}</h4>
                    <span className="text-[10px] text-zinc-500">{post.time}</span>
                  </div>
                </div>
              </div>
              
              <div className="relative aspect-square w-full bg-zinc-800">
                <img src={post.image} alt="Fan post" className="w-full h-full object-cover" />
              </div>
              
              <div className="p-4">
                <div className="flex items-center gap-4 mb-3">
                  <button 
                    onClick={() => handleUpvote(post.id)}
                    className={`flex items-center gap-1.5 text-sm font-bold transition-colors ${
                      isUpvoted ? 'text-red-500' : 'text-zinc-400 hover:text-white'
                    }`}
                  >
                    <Heart size={20} className={isUpvoted ? 'fill-red-500' : ''} />
                    <span>{post.upvotes}</span>
                  </button>
                </div>
                <p className="text-sm text-zinc-300 leading-relaxed">
                  <span className="font-bold text-white ml-2">{post.author}</span>
                  {post.caption}
                </p>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
