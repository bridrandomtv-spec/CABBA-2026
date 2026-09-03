import { useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell } from 'recharts';
import { Trophy, Target, TrendingUp, CheckCircle, Flame, Star, ChevronDown, Activity, ChevronLeft, ChevronRight, X, Share2 } from 'lucide-react';

export default function MatchPredictions() {
  const [predicted, setPredicted] = useState(false);
  const [homeScore, setHomeScore] = useState(0);
  const [awayScore, setAwayScore] = useState(0);

  const leaderboard = [
    { rank: 1, name: 'سفيان البرجي', points: 1250, accuracy: 82, badge: '🔥' },
    { rank: 2, name: 'عاشق الكابا', points: 1120, accuracy: 75, badge: '⭐' },
    { rank: 3, name: 'أمين CABBA', points: 980, accuracy: 68, badge: '⚡' },
    { rank: 4, name: 'أحمد 34', points: 850, accuracy: 62, badge: '' },
    { rank: 5, name: 'محمد الأمين', points: 790, accuracy: 58, badge: '' },
    { rank: 142, name: 'أنت', points: 320, accuracy: 45, badge: '' },
  ];
  
  const accuracyData = [
    { name: 'المتصدر', accuracy: 82, fill: '#eab308' },
    { name: 'المتوسط', accuracy: 55, fill: '#71717a' },
    { name: 'أنت', accuracy: 45, fill: '#ef4444' },
  ];

  const handlePredict = () => {
    setPredicted(true);
  };

  const handleShare = async () => {
    const shareData = {
      title: 'توقع المباراة',
      text: `لقد توقعت فوز الكابا بـ ${homeScore} - ${awayScore}! شارك توقعاتك عبر تطبيق الجراد الأصفر.`,
      url: window.location.href,
    };

    try {
      if (navigator.share) {
        await navigator.share(shareData);
      } else {
        // Fallback
        const xUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(shareData.text)}&url=${encodeURIComponent(shareData.url)}`;
        window.open(xUrl, '_blank');
      }
    } catch (err) {
      console.log('Error sharing:', err);
    }
  };

  return (
    <div className="space-y-4">
      {/* Prediction Card */}
      <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-5 shadow-lg relative overflow-hidden">
        <div className="absolute top-0 right-0 w-32 h-32 bg-yellow-500/10 rounded-full blur-2xl translate-x-10 -translate-y-10"></div>
        
        <div className="relative z-10 flex items-center gap-3 mb-6">
          <div className="w-12 h-12 bg-yellow-500/10 rounded-full flex items-center justify-center text-yellow-500">
            <Target size={24} />
          </div>
          <div>
            <h3 className="font-bold text-white text-lg">توقع النتيجة</h3>
            <p className="text-xs text-zinc-400">اربح 50 نقطة للتوقع الصحيح</p>
          </div>
        </div>

        {!predicted ? (
          <div className="space-y-6 relative z-10">
            <div className="flex justify-between items-center bg-zinc-800/50 p-4 rounded-xl border border-zinc-700/50">
              {/* Home Team */}
              <div className="flex flex-col items-center gap-2">
                <div className="w-12 h-12 bg-zinc-800 rounded-full border border-zinc-600 flex items-center justify-center">
                  <span className="text-sm font-bold text-white">C</span>
                </div>
                <span className="font-bold text-white text-sm">الكابا</span>
                <div className="flex items-center gap-2 mt-2">
                  <button onClick={() => setHomeScore(Math.max(0, homeScore - 1))} className="w-8 h-8 rounded-full bg-zinc-700 flex items-center justify-center text-white hover:bg-zinc-600 transition-colors"><ChevronRight size={16}/></button>
                  <span className="text-2xl font-black text-white w-6 text-center">{homeScore}</span>
                  <button onClick={() => setHomeScore(homeScore + 1)} className="w-8 h-8 rounded-full bg-zinc-700 flex items-center justify-center text-white hover:bg-zinc-600 transition-colors"><ChevronLeft size={16}/></button>
                </div>
              </div>

              <div className="flex flex-col items-center justify-center h-full pt-4">
                 <span className="text-zinc-500 text-xs font-bold mb-2">ضد</span>
              </div>

              {/* Away Team */}
              <div className="flex flex-col items-center gap-2">
                <div className="w-12 h-12 bg-zinc-800 rounded-full border border-zinc-600 flex items-center justify-center">
                  <span className="text-sm font-bold text-white">M</span>
                </div>
                <span className="font-bold text-white text-sm">المنافس</span>
                <div className="flex items-center gap-2 mt-2">
                  <button onClick={() => setAwayScore(Math.max(0, awayScore - 1))} className="w-8 h-8 rounded-full bg-zinc-700 flex items-center justify-center text-white hover:bg-zinc-600 transition-colors"><ChevronRight size={16}/></button>
                  <span className="text-2xl font-black text-white w-6 text-center">{awayScore}</span>
                  <button onClick={() => setAwayScore(awayScore + 1)} className="w-8 h-8 rounded-full bg-zinc-700 flex items-center justify-center text-white hover:bg-zinc-600 transition-colors"><ChevronLeft size={16}/></button>
                </div>
              </div>
            </div>
            
            <button 
              onClick={handlePredict}
              className="w-full bg-yellow-500 hover:bg-yellow-400 text-black text-sm font-bold py-3.5 rounded-xl transition-all shadow-[0_0_20px_rgba(234,179,8,0.3)] hover:shadow-[0_0_25px_rgba(234,179,8,0.5)] flex items-center justify-center gap-2"
            >
              تأكيد التوقع <Target size={18} />
            </button>
          </div>
        ) : (
          <div className="py-6 animate-in zoom-in duration-300 text-center relative z-10">
            <div className="w-16 h-16 bg-green-500/20 rounded-full flex items-center justify-center mx-auto mb-4 border border-green-500/50">
              <CheckCircle className="text-green-500 w-8 h-8" />
            </div>
            <h4 className="font-bold text-white text-lg mb-2">تم تسجيل توقعك!</h4>
            <div className="flex items-center justify-center gap-4 my-4">
                <span className="font-bold text-white text-lg">الكابا {homeScore}</span>
                <span className="text-zinc-500 text-sm">-</span>
                <span className="font-bold text-white text-lg">{awayScore} المنافس</span>
            </div>
            <p className="text-xs text-zinc-400 max-w-[250px] mx-auto mb-6">سيتم إضافة 50 نقطة إلى رصيدك إذا كان توقعك صحيحاً بعد نهاية المباراة.</p>
            
            <div className="flex flex-col items-center gap-3">
              <button 
                onClick={handleShare}
                className="w-full bg-zinc-800 hover:bg-zinc-700 border border-zinc-700 text-white text-sm font-bold py-2.5 rounded-xl transition-colors flex items-center justify-center gap-2 max-w-[200px]"
              >
                <Share2 size={16} /> شارك التوقع
              </button>
              <button 
                onClick={() => {setPredicted(false); setHomeScore(0); setAwayScore(0);}}
                className="text-xs text-zinc-500 hover:text-white underline underline-offset-4 transition-colors"
              >
                تغيير التوقع
              </button>
            </div>
          </div>
        )}
      </div>

      {/* Leaderboard Card */}
      <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-5 shadow-lg relative overflow-hidden">
        <div className="flex items-center justify-between mb-5">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-yellow-500/10 rounded-full flex items-center justify-center text-yellow-500">
                <Trophy size={20} />
              </div>
              <h3 className="font-bold text-white text-md">لوحة الصدارة</h3>
            </div>
            <button onClick={() => alert('هذه الخاصية ستتوفر قريباً!')} className="text-xs text-zinc-400 flex items-center gap-1 hover:text-white transition-colors">
                هذا الأسبوع <ChevronDown size={14} />
            </button>
        </div>

        <div className="space-y-3">
            {leaderboard.map((user, index) => (
                <div key={user.rank} className={`flex items-center justify-between p-3 rounded-xl border ${index === 0 ? 'bg-yellow-500/5 border-yellow-500/20' : 'bg-zinc-800/30 border-zinc-700/30'}`}>
                    <div className="flex items-center gap-3">
                        <div className={`w-8 h-8 rounded-full flex items-center justify-center font-bold text-xs ${
                            index === 0 ? 'bg-yellow-500 text-black shadow-[0_0_10px_rgba(234,179,8,0.3)]' : 
                            index === 1 ? 'bg-zinc-300 text-zinc-900' : 
                            index === 2 ? 'bg-amber-700 text-white' : 
                            'bg-zinc-800 text-zinc-400 border border-zinc-700'
                        }`}>
                            {user.rank}
                        </div>
                        <div>
                            <div className="flex items-center gap-1">
                                <span className={`font-bold text-sm ${index === 0 ? 'text-yellow-500' : 'text-white'}`}>{user.name}</span>
                                {user.badge && <span className="text-xs">{user.badge}</span>}
                            </div>
                        </div>
                    </div>
                    <div className="flex items-center gap-1.5">
                        <span className="font-black text-white text-sm">{user.points}</span>
                        <span className="text-[10px] text-zinc-500 font-bold">نقطة</span>
                    </div>
                </div>
            ))}
        </div>
      </div>
    </div>
  );
}
