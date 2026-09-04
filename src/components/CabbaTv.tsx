import { useState, useEffect } from 'react';
import { Play, Tv, Eye, Clock, Search, Filter } from 'lucide-react';
import { collection, query, orderBy, onSnapshot, doc, updateDoc, increment } from 'firebase/firestore';
import { db } from '../lib/firebase';
import { Video } from './admin/AdminVideos';

export default function CabbaTv() {
  const [activeCategory, setActiveCategory] = useState('all');
  const [searchQuery, setSearchQuery] = useState('');
  const [videos, setVideos] = useState<Video[]>([]);
  
  useEffect(() => {
    const q = query(collection(db, 'videos'), orderBy('createdAt', 'desc'));
    const un = onSnapshot(q, (snapshot) => {
      const data: Video[] = [];
      snapshot.forEach(doc => {
        const v = { id: doc.id, ...doc.data() } as Video;
        if (v.published) data.push(v);
      });
      setVideos(data);
    });
    return () => un();
  }, []);

  const handlePlay = async (v: Video) => {
    window.open(v.videoUrl, '_blank');
    try {
      await updateDoc(doc(db, 'videos', v.id), { views: increment(1) });
    } catch(e) {}
  };

  return (
    <div className="p-4 space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-500" dir="rtl">
      <div className="flex items-center gap-3 mb-2">
        <div className="w-10 h-10 bg-yellow-500/10 rounded-full flex items-center justify-center text-yellow-500 shadow-[0_0_15px_rgba(234,179,8,0.2)]">
          <Tv size={20} />
        </div>
        <div>
          <h2 className="font-bold text-white text-xl">كابا TV</h2>
          <p className="text-xs text-zinc-400">تغطية حصرية وبث مباشر</p>
        </div>
      </div>

      <div className="flex gap-2">
        <div className="relative flex-1">
          <Search className="absolute right-3 top-1/2 -translate-y-1/2 text-zinc-500" size={16} />
          <input 
            type="text" 
            placeholder="بحث عن فيديو..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full bg-zinc-900 border border-zinc-800 rounded-xl py-2 pr-10 pl-4 text-white text-sm focus:border-yellow-500 outline-none"
          />
        </div>
        <button className="bg-zinc-900 border border-zinc-800 text-zinc-400 p-2 rounded-xl hover:text-white">
          <Filter size={18} />
        </button>
      </div>

      <div className="space-y-4">
        {videos
          .filter(v => activeCategory === 'all' || v.category === activeCategory)
          .filter(v => v.title.includes(searchQuery) || v.description.includes(searchQuery))
          .map(v => (
          <div key={v.id} className="bg-zinc-900 border border-zinc-800 rounded-2xl overflow-hidden group">
            <div className="relative h-48 bg-zinc-800 cursor-pointer" onClick={() => handlePlay(v)}>
              <img 
                src={v.thumbnail || `https://images.unsplash.com/photo-1574629810360-7efbb4b2fac0?w=800&h=400&fit=crop&q=80&${v.id}`}
                alt={v.title}
                className="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity"
              />
              <div className="absolute inset-0 flex items-center justify-center pointer-events-none">
                <div className="w-14 h-14 bg-yellow-500/90 text-black rounded-full flex items-center justify-center backdrop-blur-sm group-hover:scale-110 transition-transform shadow-[0_0_20px_rgba(234,179,8,0.4)]">
                  <Play size={24} className="fill-current ml-1" />
                </div>
              </div>
            </div>
            <div className="p-4">
              <h3 className="font-bold text-white text-sm mb-2 group-hover:text-yellow-500 transition-colors line-clamp-2 cursor-pointer" onClick={() => handlePlay(v)}>
                {v.title}
              </h3>
              <div className="flex items-center gap-4 text-xs text-zinc-500">
                <div className="flex items-center gap-1">
                  <Eye size={14} />
                  <span>{v.views}</span>
                </div>
                <div className="flex items-center gap-1">
                  <Clock size={14} />
                  <span>جديد</span>
                </div>
                <div className="bg-zinc-800 px-2 py-1 rounded text-zinc-400 mr-auto">
                  {v.category}
                </div>
              </div>
            </div>
          </div>
        ))}
        {videos.length === 0 && (
          <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-8 flex flex-col items-center justify-center text-center">
            <Tv size={48} className="text-zinc-700 mb-4" />
            <h4 className="font-bold text-zinc-400">لا توجد فيديوهات</h4>
          </div>
        )}
      </div>
    </div>
  );
}
