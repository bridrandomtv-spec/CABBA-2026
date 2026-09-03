import { useState } from 'react';
import { Play, Pause, Music, Heart, Share2, AlignCenter } from 'lucide-react';

export default function ChantsLibrary() {
  const [playingId, setPlayingId] = useState<string | null>(null);
  const [showLyrics, setShowLyrics] = useState(false);

  const audioList = [
    { id: 'a1', title: 'كابا يا كابا (الجراد الأصفر)', duration: '4:30', plays: '12K', lyrics: 'كابا يا كابا...\nيا عمري يا حياتي\nنموت عليك يا البريجية\nان شاء الله زاهية' },
    { id: 'a2', title: 'أهلي البرج برجنا', duration: '3:15', plays: '8.5K', lyrics: 'أهلي البرج برجنا\nوالكابا هي حبنا\nمن الصغرة ربينا\nعلى الوانك يا زينة' },
    { id: 'a3', title: 'شجعوا الفريق - أهازيج المدرج 20', duration: '5:45', plays: '20K', lyrics: 'شجعوا الفريق\nيا لولاد جيبوها\nفي كل طريق\nالراية نرفعوها' },
    { id: 'a4', title: 'فدائيون يا بيبان', duration: '4:10', plays: '15K', lyrics: 'فدائيون فدائيون\nنحن للكابا عاشقون\nفي كل مكان حاضرون\nولألوانك رافعون' },
  ];

  const currentAudio = audioList.find(a => a.id === playingId) || audioList[0];

  const handleShare = async (audio: typeof audioList[0]) => {
    try {
      if (navigator.share) {
        await navigator.share({
          title: audio.title,
          text: `اسمع رائعة المدرج 20: ${audio.title}\n\n${audio.lyrics}\n\n`,
          url: window.location.href,
        });
      }
    } catch (error) {
      console.log('Error sharing', error);
    }
  };

  return (
    <div className="p-4 space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-500" dir="rtl">
      
      {/* Header */}
      <div className="flex items-center gap-3 mb-2">
        <div className="w-10 h-10 bg-yellow-500/10 rounded-full flex items-center justify-center text-yellow-500 shadow-[0_0_15px_rgba(234,179,8,0.2)]">
          <Music size={20} />
        </div>
        <div>
          <h2 className="font-bold text-white text-xl">أهازيج الجراد الأصفر</h2>
          <p className="text-xs text-zinc-400">صوت المدرج 20 في جيبك</p>
        </div>
      </div>

      <div className="space-y-4">
        {/* Player Area */}
        <div className="bg-zinc-900 rounded-3xl p-6 flex flex-col items-center justify-center aspect-square border border-zinc-800 relative overflow-hidden shadow-2xl transition-all duration-500">
            <div className="absolute top-0 right-0 w-40 h-40 bg-yellow-500/5 rounded-full blur-3xl translate-x-10 -translate-y-10 pointer-events-none"></div>
            <div className="absolute bottom-0 left-0 w-32 h-32 bg-yellow-500/5 rounded-full blur-3xl -translate-x-10 translate-y-10 pointer-events-none"></div>
            
            {!showLyrics ? (
              <>
                <div className="w-36 h-36 rounded-full border-4 border-zinc-800 flex items-center justify-center bg-black relative mb-8 shadow-[0_0_40px_rgba(234,179,8,0.2)] group">
                  <div className="absolute inset-0 rounded-full border-2 border-yellow-500 border-t-transparent animate-spin" style={{ animationDuration: '3s', animationPlayState: playingId ? 'running' : 'paused' }}></div>
                  <div className="absolute inset-0 rounded-full border border-yellow-500/30 border-b-transparent animate-spin-reverse" style={{ animationDuration: '5s', animationPlayState: playingId ? 'running' : 'paused' }}></div>
                  <Music size={48} className="text-yellow-500 drop-shadow-[0_0_15px_rgba(234,179,8,0.8)]" />
                </div>
                <h3 className="font-bold text-white text-2xl text-center mb-2 tracking-wide leading-tight">{currentAudio.title}</h3>
                <p className="text-zinc-400 text-sm mb-8 font-medium">المدرج رقم 20</p>
                
                <div className="flex items-center gap-8 z-10 w-full justify-center px-4">
                  <button 
                    onClick={() => handleShare(currentAudio)}
                    className="text-zinc-500 hover:text-white transition-colors p-2"
                  >
                    <Share2 size={24} />
                  </button>
                  <button 
                    onClick={() => setPlayingId(playingId ? null : currentAudio.id)}
                    className="w-16 h-16 bg-yellow-500 rounded-full flex items-center justify-center text-black hover:scale-105 active:scale-95 transition-all shadow-[0_0_20px_rgba(234,179,8,0.5)]"
                  >
                    {playingId ? <Pause size={28} className="fill-current" /> : <Play size={28} className="fill-current translate-x-[-2px]" />}
                  </button>
                  <button onClick={() => setShowLyrics(true)} className="text-zinc-500 hover:text-yellow-500 transition-colors p-2 relative">
                    <AlignCenter size={24} />
                    <span className="absolute -top-1 -right-1 w-2 h-2 bg-yellow-500 rounded-full"></span>
                  </button>
                </div>
                
                <div className="w-full mt-8">
                   <div className="w-full h-1 bg-zinc-800 rounded-full overflow-hidden">
                     <div className="h-full bg-yellow-500 w-[35%] rounded-full relative">
                        <div className="absolute right-0 top-1/2 -translate-y-1/2 w-2 h-2 bg-white rounded-full shadow-[0_0_5px_rgba(255,255,255,1)]"></div>
                     </div>
                   </div>
                   <div className="flex justify-between mt-2 text-[10px] text-zinc-500 font-bold">
                     <span>1:15</span>
                     <span>{currentAudio.duration}</span>
                   </div>
                </div>
              </>
            ) : (
              <div className="w-full h-full flex flex-col z-10 animate-in zoom-in-95 duration-300">
                <div className="flex justify-between items-center mb-6">
                  <h3 className="font-bold text-yellow-500 text-lg border-b border-yellow-500/20 pb-2 inline-block">{currentAudio.title}</h3>
                  <button onClick={() => setShowLyrics(false)} className="text-zinc-400 hover:text-white text-xs bg-zinc-800/80 px-3 py-1.5 rounded-lg border border-zinc-700 transition-colors">إغلاق الكلمات</button>
                </div>
                <div className="flex-1 overflow-y-auto space-y-5 text-center pb-8 scrollbar-hide">
                  {currentAudio.lyrics.split('\n').map((line, i) => (
                    <p key={i} className={`text-xl font-bold transition-all duration-500 ${i === 1 ? 'text-white scale-110 drop-shadow-[0_0_10px_rgba(255,255,255,0.4)]' : 'text-zinc-500 opacity-60'}`}>
                      {line}
                    </p>
                  ))}
                  <p className="text-zinc-500 opacity-60 text-xl font-bold">...</p>
                </div>
                <div className="absolute bottom-0 left-0 right-0 h-24 bg-gradient-to-t from-zinc-900 to-transparent pointer-events-none z-20"></div>
              </div>
            )}
        </div>

        {/* List Area */}
        <div className="space-y-3 pb-8">
          <h3 className="font-bold text-white mb-2 text-sm">المكتبة الصوتية</h3>
          {audioList.map((audio) => (
            <div key={audio.id} className={`bg-zinc-900/80 border ${playingId === audio.id ? 'border-yellow-500 bg-zinc-900 shadow-[0_0_15px_rgba(234,179,8,0.1)]' : 'border-zinc-800/50'} rounded-2xl p-4 flex items-center gap-4 hover:border-yellow-500/50 transition-all cursor-pointer group`} onClick={() => setPlayingId(playingId === audio.id ? null : audio.id)}>
              <button onClick={() => alert('هذه الخاصية ستتوفر قريباً!')} 
                className={`w-12 h-12 rounded-full flex items-center justify-center flex-none transition-colors ${playingId === audio.id ? 'bg-yellow-500 text-black shadow-lg' : 'bg-zinc-800 text-yellow-500 group-hover:bg-zinc-700'}`}
              >
                {playingId === audio.id ? <Pause size={18} className="fill-current" /> : <Play size={18} className="fill-current translate-x-[-1px]" />}
              </button>
              <div className="flex-1 min-w-0">
                <h4 className={`text-sm font-bold truncate mb-1 transition-colors ${playingId === audio.id ? 'text-yellow-500' : 'text-zinc-100 group-hover:text-white'}`}>{audio.title}</h4>
                <div className="flex items-center gap-3">
                  <span className="text-xs text-zinc-500 font-medium">{audio.duration}</span>
                  <span className="text-[10px] text-zinc-600">•</span>
                  <span className="text-xs text-zinc-500 font-medium flex items-center gap-1"><Heart size={10} className="fill-current opacity-50"/> {audio.plays}</span>
                </div>
              </div>
              <button className="text-zinc-500 hover:text-white p-2 transition-colors hover:scale-110" onClick={(e) => { e.stopPropagation(); handleShare(audio); }}>
                <Share2 size={16} />
              </button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
