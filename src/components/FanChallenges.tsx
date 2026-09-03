import { useState } from 'react';
import { Target, CheckCircle2, Award, Zap, Camera, Mic, Share2 } from 'lucide-react';

interface Challenge {
  id: number;
  title: string;
  description: string;
  points: number;
  completed: boolean;
  icon: any;
  actionText?: string;
}

export default function FanChallenges() {
  const [challenges, setChallenges] = useState<Challenge[]>([
    { 
      id: 1, 
      title: 'شاركنا ألوان الكابا', 
      description: 'انشر صورة لك بقميص الفريق في عدسة الجماهير', 
      points: 150, 
      completed: false, 
      icon: Camera,
      actionText: 'شارك صورتك'
    },
    { 
      id: 2, 
      title: 'فرحة الفوز', 
      description: 'سجل مقطع صوتي لهتافك المفضل للفريق', 
      points: 200, 
      completed: false, 
      icon: Mic,
      actionText: 'سجل الآن'
    },
    { 
      id: 3, 
      title: 'التفاعل مع المنشورات', 
      description: 'قم بالإعجاب بـ 5 منشورات في مجتمع الكابا', 
      points: 50, 
      completed: true, 
      icon: Share2 
    },
  ]);

  const [claimed, setClaimed] = useState<Record<number, boolean>>({});

  const handleClaim = (id: number) => {
    setClaimed(prev => ({ ...prev, [id]: true }));
    // In a real app, this would update the user's total points and badges
  };

  const handleAction = (id: number) => {
    if (id === 1) {
      alert("سيتم فتح الكاميرا قريباً لالتقاط صورتك!");
    } else if (id === 2) {
      alert("تم تسجيل المقطع الصوتي بنجاح! لقد أكملت التحدي.");
    }
    
    // Mark as completed
    setChallenges(prev => prev.map(c => 
      c.id === id ? { ...c, completed: true } : c
    ));
  };


  return (
    <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-5 shadow-sm">
      <div className="flex items-center justify-between mb-4">
        <div>
          <h3 className="font-bold text-white text-lg flex items-center gap-2">
            <Target className="text-yellow-500" size={20} />
            تحديات الأسبوع
          </h3>
          <p className="text-xs text-zinc-400 mt-1">أكمل المهام لزيادة نقاطك وترقية أوسمتك</p>
        </div>
        <span className="text-xs text-yellow-500 font-bold bg-yellow-500/10 px-3 py-1.5 rounded-full border border-yellow-500/20">
          جديد
        </span>
      </div>
      
      <div className="space-y-3">
        {challenges.map((challenge) => {
          const isClaimed = claimed[challenge.id];
          return (
            <div key={challenge.id} className={`flex flex-col p-4 rounded-xl border transition-colors ${
              challenge.completed 
                ? isClaimed 
                  ? 'bg-zinc-800/30 border-zinc-700/50 opacity-80' 
                  : 'bg-green-500/10 border-green-500/30' 
                : 'bg-zinc-800/50 border-zinc-700/50 hover:border-zinc-600'
            }`}>
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <div className={`w-10 h-10 rounded-full flex items-center justify-center shrink-0 ${
                    challenge.completed 
                      ? 'bg-green-500/20 text-green-500' 
                      : 'bg-yellow-500/10 text-yellow-500'
                  }`}>
                    {challenge.completed ? <CheckCircle2 size={20} /> : <challenge.icon size={20} />}
                  </div>
                  <div>
                    <p className={`text-sm font-bold ${challenge.completed ? 'text-zinc-300' : 'text-white'} mb-1`}>
                      {challenge.title}
                    </p>
                    <p className="text-[10px] text-zinc-400 leading-relaxed">{challenge.description}</p>
                  </div>
                </div>
                <div className="flex flex-col items-end gap-1 shrink-0 ml-2">
                  <span className={`text-sm font-black ${challenge.completed && !isClaimed ? 'text-green-500' : 'text-yellow-500'}`}>
                    +{challenge.points}
                  </span>
                  <span className="text-[10px] text-zinc-500 font-bold">نقطة</span>
                </div>
              </div>
              
              {!challenge.completed && challenge.actionText && (
                <button onClick={() => handleAction(challenge.id)} className="mt-4 w-full bg-zinc-800 hover:bg-zinc-700 text-white text-xs font-bold py-2 rounded-lg transition-colors border border-zinc-700 group hover:border-yellow-500/50">
                  <span className="group-hover:text-yellow-500 transition-colors">{challenge.actionText}</span>
                </button>
              )}
              
              {challenge.completed && !isClaimed && (
                <button 
                  onClick={() => handleClaim(challenge.id)}
                  className="mt-4 w-full bg-green-500 hover:bg-green-400 text-black text-xs font-bold py-2 rounded-lg transition-colors shadow-[0_0_15px_rgba(34,197,94,0.3)] flex items-center justify-center gap-2"
                >
                  <Award size={16} />
                  استلام المكافأة
                </button>
              )}
              
              {challenge.completed && isClaimed && (
                <div className="mt-4 w-full text-center text-[10px] text-green-500 font-bold">
                  تم استلام النقاط بنجاح
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}
