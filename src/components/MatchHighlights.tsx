import { Play, Calendar, Star } from 'lucide-react';

import { useState } from 'react';
import { X } from 'lucide-react';
export default function MatchHighlights() {
  const [playingId, setPlayingId] = useState<string | null>(null);
  const highlights = [
    { 
      id: '1', 
      title: 'هدف الانتصار في الدقيقة 90', 
      match: 'الكابا ضد شبيبة القبائل', 
      date: '05 مارس', 
      duration: '1:15', 
      thumbnail: 'https://images.unsplash.com/photo-1518605368461-1ee125225026?auto=format&fit=crop&q=80&w=800&h=400' 
    },
    { 
      id: '2', 
      title: 'ملخص الشوط الأول', 
      match: 'الكابا ضد وفاق سطيف', 
      date: '28 فيفري', 
      duration: '4:30', 
      thumbnail: 'https://images.unsplash.com/photo-1431324155629-1a6d0a6eb600?auto=format&fit=crop&q=80&w=800&h=400' 
    },
    { 
      id: '3', 
      title: 'تألق الحارس في ضربة الجزاء', 
      match: 'الكابا ضد مولودية الجزائر', 
      date: '20 فيفري', 
      duration: '0:45', 
      thumbnail: 'https://images.unsplash.com/photo-1579952363873-27f3bade9f55?auto=format&fit=crop&q=80&w=800&h=400' 
    },
  ];

  return (
    <div className="space-y-4 animate-in fade-in slide-in-from-right-4">
      <div className="flex items-center justify-between mb-2 mt-6">
        <h3 className="font-bold text-white text-sm flex items-center gap-2">
          <Star size={16} className="text-yellow-500" /> ملخصات وأهداف
        </h3>
      </div>
      
      <div className="flex overflow-x-auto gap-4 pb-4 -mx-4 px-4 snap-x [&::-webkit-scrollbar]:hidden [-ms-overflow-style:none] [scrollbar-width:none]">
        {highlights.map(highlight => (
          <div key={highlight.id} onClick={() => setPlayingId(highlight.id)} className="w-[280px] flex-none bg-zinc-900 border border-zinc-800 rounded-2xl overflow-hidden group snap-center shadow-lg cursor-pointer">
            <div className="relative aspect-video">
              <img src={highlight.thumbnail} alt={highlight.title} className="w-full h-full object-cover" />
              <div className="absolute inset-0 bg-black/40 group-hover:bg-black/20 transition-colors"></div>
              <div className="absolute inset-0 flex items-center justify-center">
                <div className="w-12 h-12 rounded-full bg-yellow-500 text-black flex items-center justify-center shadow-[0_0_15px_rgba(234,179,8,0.5)] scale-90 group-hover:scale-100 transition-transform">
                  <Play size={20} className="fill-current translate-x-[-1px]" />
                </div>
              </div>
              <span className="absolute bottom-2 left-2 bg-black/80 text-zinc-50 text-[10px] px-2 py-1 rounded font-medium backdrop-blur-sm z-20">
                {highlight.duration}
              </span>
            </div>
            <div className="p-4">
              <h4 className="text-sm font-bold text-white mb-2 line-clamp-2">{highlight.title}</h4>
              <div className="flex items-center justify-between text-[10px] text-zinc-400">
                <span className="font-medium text-yellow-500/80">{highlight.match}</span>
                <div className="flex items-center gap-1">
                  <Calendar size={10} />
                  <span>{highlight.date}</span>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
      {playingId && (
        <div className="fixed inset-0 z-[100] bg-black/90 flex flex-col items-center justify-center p-4 animate-in fade-in duration-300">
          <button 
            onClick={() => setPlayingId(null)}
            className="absolute top-safe right-4 w-10 h-10 bg-zinc-800/50 rounded-full flex items-center justify-center text-white hover:bg-zinc-700 transition-colors z-50"
          >
            <X size={24} />
          </button>
          
          <div className="w-full max-w-3xl aspect-video bg-black rounded-2xl overflow-hidden border border-zinc-800 shadow-[0_0_50px_rgba(234,179,8,0.15)] relative flex items-center justify-center group">
             <div className="absolute inset-0 flex flex-col items-center justify-center gap-4 text-zinc-500">
                <Play size={48} className="text-zinc-600 group-hover:text-yellow-500 transition-colors" />
                <p className="font-bold text-sm">مشغل الفيديو (نسخة تجريبية)</p>
             </div>
             
             {/* Fake controls bar */}
             <div className="absolute bottom-0 left-0 right-0 h-12 bg-gradient-to-t from-black/80 to-transparent flex items-end p-4">
               <div className="w-full h-1 bg-zinc-800 rounded-full overflow-hidden">
                 <div className="w-1/3 h-full bg-yellow-500 rounded-full"></div>
               </div>
             </div>
          </div>
          
          <div className="w-full max-w-3xl mt-4 text-right">
             <h3 className="font-bold text-white text-lg">
                {highlights.find(h => h.id === playingId)?.title}
             </h3>
             <p className="text-zinc-400 text-sm mt-1">
                {highlights.find(h => h.id === playingId)?.match}
             </p>
          </div>
        </div>
      )}
    </div>
  );
}
