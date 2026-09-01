import { useState } from 'react';
import { Play, Share2, Tv, Radio, Pause, Volume2 } from 'lucide-react';
import MatchHighlights from './MatchHighlights';

export default function CabbaTv() {
  const [isRadioPlaying, setIsRadioPlaying] = useState(false);

  const videoList = [
    { id: 'v1', title: 'كواليس التدريبات: تحضيرات الديربي', duration: '10:20', views: '45K', category: 'خلف الكواليس' },
    { id: 'v2', title: 'دَخْلَة الجراد الأصفر ضد الوفاق', duration: '2:15', views: '110K', category: 'المدرجات' },
    { id: 'v3', title: 'لقاء حصري مع أسطورة الجيل الذهبي', duration: '15:30', views: '32K', category: 'لقاءات' },
  ];

  return (
    <div className="p-4 space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-500" dir="rtl">
      
      {/* Header */}
      <div className="flex items-center gap-3 mb-2">
        <div className="w-10 h-10 bg-yellow-500/10 rounded-full flex items-center justify-center text-yellow-500 shadow-[0_0_15px_rgba(234,179,8,0.2)]">
          <Tv size={20} />
        </div>
        <div>
          <h2 className="font-bold text-white text-xl">كابا TV</h2>
          <p className="text-xs text-zinc-400">تغطية حصرية وبث مباشر</p>
        </div>
      </div>

      <div className="space-y-4">
        {/* Live Radio */}
        <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-5 shadow-lg relative overflow-hidden">
          <div className="absolute top-0 right-0 w-32 h-32 bg-yellow-500/10 rounded-full blur-2xl translate-x-10 -translate-y-10"></div>
          <div className="relative z-10 flex flex-col gap-4">
            <div className="flex justify-between items-start">
              <div className="flex items-center gap-3">
                <div className="relative">
                  <div className="w-12 h-12 bg-zinc-800 rounded-full border border-yellow-500/50 flex items-center justify-center text-yellow-500 shadow-[0_0_15px_rgba(234,179,8,0.2)]">
                    <Radio size={24} />
                  </div>
                  <span className="absolute -bottom-1 -right-1 flex h-3 w-3">
                    <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-red-500 opacity-75"></span>
                    <span className="relative inline-flex rounded-full h-3 w-3 bg-red-500"></span>
                  </span>
                </div>
                <div>
                  <h3 className="font-bold text-white text-lg">راديو الكابا</h3>
                  <p className="text-xs text-zinc-400">تغطية مباشرة لأخبار النادي</p>
                </div>
              </div>
              <span className="bg-red-500/10 text-red-500 text-[10px] font-bold px-2 py-1 rounded-md border border-red-500/20 flex items-center gap-1 shadow-sm">
                مباشر <span className="w-1.5 h-1.5 bg-red-500 rounded-full animate-pulse"></span>
              </span>
            </div>
            
            <div className="flex items-center gap-4 bg-zinc-800/50 p-3 rounded-xl border border-zinc-700/50">
              <button 
                onClick={() => setIsRadioPlaying(!isRadioPlaying)}
                className="w-10 h-10 bg-yellow-500 rounded-full flex items-center justify-center text-black flex-none hover:scale-105 transition-transform shadow-[0_0_15px_rgba(234,179,8,0.3)]"
              >
                {isRadioPlaying ? <Pause size={20} className="fill-current" /> : <Play size={20} className="fill-current translate-x-[-1px]" />}
              </button>
              
              <div className="flex-1 overflow-hidden">
                {isRadioPlaying ? (
                  <div className="flex items-center justify-center gap-1 h-6 w-full">
                    {[...Array(15)].map((_, i) => (
                      <div 
                        key={i} 
                        className="w-1.5 bg-yellow-500 rounded-full animate-[pulse_1s_ease-in-out_infinite]"
                        style={{ 
                          height: `${Math.max(20, Math.random() * 100)}%`,
                          animationDelay: `${i * 0.1}s`,
                          animationDuration: `${0.5 + Math.random() * 0.5}s`
                        }}
                      ></div>
                    ))}
                  </div>
                ) : (
                  <div className="h-6 flex items-center">
                    <div className="w-full h-1 bg-zinc-700/50 rounded-full"></div>
                  </div>
                )}
              </div>
              
              <button className="text-zinc-400 hover:text-white transition-colors">
                <Volume2 size={20} />
              </button>
            </div>
          </div>
        </div>

        <MatchHighlights />

        <h3 className="font-bold text-white mb-2 mt-6 text-sm">أحدث الفيديوهات</h3>
        {videoList.map((video) => (
          <div key={video.id} className="bg-zinc-900 border border-zinc-800 rounded-xl overflow-hidden group">
            <div className="aspect-video bg-zinc-800 relative flex items-center justify-center cursor-pointer overflow-hidden">
              <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent z-10"></div>
              <div className="absolute top-2 right-2 z-20">
                <span className="bg-yellow-500 text-black text-[10px] font-bold px-2 py-0.5 rounded shadow">
                  {video.category}
                </span>
              </div>
              <div className="w-14 h-14 rounded-full bg-yellow-500 text-black flex items-center justify-center z-20 shadow-[0_0_20px_rgba(234,179,8,0.4)] scale-90 group-hover:scale-100 transition-transform">
                <Play size={24} className="fill-current translate-x-[-1px]" />
              </div>
              <span className="absolute bottom-2 left-2 bg-black/80 text-zinc-50 text-[10px] px-2 py-1 rounded font-medium z-20 backdrop-blur-sm">
                {video.duration}
              </span>
            </div>
            <div className="p-4 flex items-start justify-between gap-4">
              <div>
                <h4 className="text-sm font-bold text-white mb-1 line-clamp-2 leading-tight">{video.title}</h4>
                <p className="text-xs text-zinc-400">{video.views} مشاهدة</p>
              </div>
              <button className="text-zinc-400 hover:text-white p-2 bg-zinc-800/50 rounded-full transition-colors">
                <Share2 size={16} />
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
