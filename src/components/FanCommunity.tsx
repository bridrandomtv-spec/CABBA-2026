import { useState } from 'react';
import FanChallenges from './FanChallenges';
import { Heart, MessageSquare, Share2, Image as ImageIcon, Send, User } from 'lucide-react';

interface Post {
  id: string;
  author: string;
  avatar: string;
  time: string;
  content: string;
  imageUrl?: string;
  likes: number;
  comments: number;
  isLiked: boolean;
}

export default function FanCommunity() {
  const [posts, setPosts] = useState<Post[]>([
    {
      id: '1',
      author: 'أحمد الكاباوي',
      avatar: 'A',
      time: 'قبل ساعتين',
      content: 'أجواء رائعة اليوم في المدرجات! الفريق قدم أداء خرافي، النقاط الثلاث هي الأهم. الجراد الأصفر دائماً في الموعد 💛🖤',
      likes: 124,
      comments: 18,
      isLiked: false,
    },
    {
      id: '2',
      author: 'رياض 34',
      avatar: 'R',
      time: 'قبل 4 ساعات',
      content: 'صور من دخلة اليوم.. الإبداع مستمر!',
      imageUrl: 'https://images.unsplash.com/photo-1508344928928-7137b29de216?auto=format&fit=crop&q=80&w=800&h=400',
      likes: 342,
      comments: 45,
      isLiked: true,
    },
    {
      id: '3',
      author: 'وليد BBA',
      avatar: 'W',
      time: 'قبل 5 ساعات',
      content: 'من هو رجل المباراة برأيكم؟ بالنسبة لي الحارس كان سداً منيعاً.',
      likes: 89,
      comments: 112,
      isLiked: false,
    }
  ]);

  const [newPostText, setNewPostText] = useState('');

  const handleLike = (postId: string) => {
    setPosts(posts.map(post => {
      if (post.id === postId) {
        return {
          ...post,
          isLiked: !post.isLiked,
          likes: post.isLiked ? post.likes - 1 : post.likes + 1
        };
      }
      return post;
    }));
  };

  const handlePost = () => {
    if (!newPostText.trim()) return;
    
    const newPost: Post = {
      id: Date.now().toString(),
      author: 'أنت',
      avatar: 'Y',
      time: 'الآن',
      content: newPostText,
      likes: 0,
      comments: 0,
      isLiked: false,
    };
    
    setPosts([newPost, ...posts]);
    setNewPostText('');
  };

  return (
    <div className="p-4 space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-500" dir="rtl">
      
      <div className="flex items-center justify-between mb-2">
        <h2 className="text-xl font-black text-white">مجتمع الكابا</h2>
        <span className="bg-yellow-500/10 text-yellow-500 text-xs font-bold px-3 py-1 rounded-full border border-yellow-500/20">
          +400 متصل الآن
        </span>
      </div>

      <FanChallenges />

      {/* New Post Input */}
      <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-4 shadow-sm">
        <div className="flex gap-3">
          <div className="w-10 h-10 rounded-full bg-zinc-800 flex items-center justify-center text-zinc-400 flex-none border border-zinc-700">
            <User size={20} />
          </div>
          <div className="flex-1">
            <textarea 
              value={newPostText}
              onChange={(e) => setNewPostText(e.target.value)}
              placeholder="شارك أفكارك، صور، أو مشاعرك مع المدرج..."
              className="w-full bg-transparent text-white text-sm resize-none outline-none min-h-[60px] placeholder:text-zinc-600"
            />
            <div className="flex justify-between items-center mt-2 pt-2 border-t border-zinc-800/50">
              <button className="text-zinc-500 hover:text-yellow-500 transition-colors p-2 rounded-full hover:bg-zinc-800/50">
                <ImageIcon size={20} />
              </button>
              <button 
                onClick={handlePost}
                disabled={!newPostText.trim()}
                className="bg-yellow-500 hover:bg-yellow-400 text-black px-4 py-1.5 rounded-full text-xs font-bold flex items-center gap-2 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <span>نشر</span>
                <Send size={14} className="rotate-180" />
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Posts Feed */}
      <div className="space-y-4">
        {posts.map(post => (
          <div key={post.id} className="bg-zinc-900 border border-zinc-800 rounded-2xl p-4 shadow-sm">
            <div className="flex items-center justify-between mb-3">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-full bg-zinc-800 flex items-center justify-center text-yellow-500 font-bold text-sm border border-zinc-700">
                  {post.avatar}
                </div>
                <div>
                  <h4 className="font-bold text-white text-sm">{post.author}</h4>
                  <p className="text-[10px] text-zinc-500">{post.time}</p>
                </div>
              </div>
              <button className="text-zinc-600 hover:text-white">...</button>
            </div>
            
            <p className="text-sm text-zinc-300 leading-relaxed mb-4 whitespace-pre-wrap">
              {post.content}
            </p>

            {post.imageUrl && (
              <div className="mb-4 rounded-xl overflow-hidden border border-zinc-800">
                <img src={post.imageUrl} alt="Post media" className="w-full h-auto object-cover max-h-[300px]" />
              </div>
            )}

            <div className="flex items-center justify-between pt-3 border-t border-zinc-800/50">
              <button 
                onClick={() => handleLike(post.id)}
                className={`flex items-center gap-2 text-xs font-bold transition-colors ${post.isLiked ? 'text-red-500' : 'text-zinc-500 hover:text-red-400'}`}
              >
                <Heart size={18} className={post.isLiked ? 'fill-current' : ''} />
                <span>{post.likes}</span>
              </button>
              
              <button className="flex items-center gap-2 text-xs font-bold text-zinc-500 hover:text-white transition-colors">
                <MessageSquare size={18} />
                <span>{post.comments}</span>
              </button>
              
              <button className="flex items-center gap-2 text-xs font-bold text-zinc-500 hover:text-white transition-colors">
                <Share2 size={18} />
                <span>مشاركة</span>
              </button>
            </div>
          </div>
        ))}
      </div>
      
    </div>
  );
}
