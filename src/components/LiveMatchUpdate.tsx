import { useState, useEffect, useRef } from 'react';
import { Clock, Activity, AlertCircle, Goal, Flag } from 'lucide-react';

interface Commentary {
  id: number;
  minute: number;
  text: string;
  type: 'neutral' | 'attack' | 'goal' | 'card' | 'corner' | 'foul';
  team?: 'home' | 'away';
}

const initialCommentary: Commentary[] = [
  { id: 10, minute: 68, text: 'خطأ لصالح المنافس في مكان خطير.', type: 'foul', team: 'away' },
  { id: 9, minute: 55, text: 'ضغط متواصل من الكابا بحثاً عن الهدف الثاني.', type: 'attack', team: 'home' },
  { id: 8, minute: 46, text: 'بداية الشوط الثاني.', type: 'neutral' },
  { id: 7, minute: 45, text: 'نهاية الشوط الأول بتقدم الكابا.', type: 'neutral' },
  { id: 6, minute: 42, text: 'جوووووول! هدف أول للكابا بعد رأسية متقنة.', type: 'goal', team: 'home' },
  { id: 5, minute: 34, text: 'بطاقة صفراء للاعب الوسط بعد تدخل خشن.', type: 'card', team: 'away' },
  { id: 4, minute: 23, text: 'ركلة ركنية لصالح الكابا بعد تسديدة قوية من خارج منطقة الجزاء.', type: 'corner', team: 'home' },
  { id: 3, minute: 12, text: 'هجمة مرتدة سريعة للمنافس ولكن المدافع يقطع الكرة ببراعة.', type: 'attack', team: 'away' },
  { id: 2, minute: 5, text: 'تمريرات قصيرة بين لاعبي الكابا في وسط الميدان لمحاولة اختراق الدفاع.', type: 'neutral', team: 'home' },
  { id: 1, minute: 1, text: 'صافرة بداية الشوط الأول.', type: 'neutral' },
];

const mockUpdates: Commentary[] = [
  { id: 11, minute: 70, text: 'تسديدة قوية من المنافس ولكن الحارس يتصدى لها ببراعة!', type: 'attack', team: 'away' },
  { id: 12, minute: 73, text: 'تبديل للكابا: دخول اللاعب رقم 7 وخروج اللاعب رقم 11.', type: 'neutral', team: 'home' },
  { id: 13, minute: 78, text: 'هجمة خطيرة للكابا تنتهي بتسديدة بجوار القائم.', type: 'attack', team: 'home' },
  { id: 14, minute: 82, text: 'بطاقة صفراء لمدافع الكابا لإضاعة الوقت.', type: 'card', team: 'home' },
  { id: 15, minute: 85, text: 'ركنية خطيرة للمنافس يتم إبعادها بصعوبة من الدفاع.', type: 'corner', team: 'away' },
  { id: 16, minute: 89, text: 'جوووووول! هدف التعادل للمنافس من تسديدة مباغتة.', type: 'goal', team: 'away' },
  { id: 17, minute: 90, text: 'الحكم يحتسب 4 دقائق وقت بدل ضائع.', type: 'neutral' },
  { id: 18, minute: 93, text: 'هجمة أخيرة للكابا... العرضية داخل المنطقة!', type: 'attack', team: 'home' },
  { id: 19, minute: 94, text: 'جوووووووووووول! هدف قاتل للكابا في الثواني الأخيرة!', type: 'goal', team: 'home' },
  { id: 20, minute: 95, text: 'نهاية المباراة بفوز مثير للكابا.', type: 'neutral' },
];

export default function LiveMatchUpdate() {
  const [commentaries, setCommentaries] = useState<Commentary[]>(initialCommentary);
  const [updateIndex, setUpdateIndex] = useState(0);
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // Mock polling service
    const interval = setInterval(() => {
      if (updateIndex < mockUpdates.length) {
        setCommentaries(prev => [mockUpdates[updateIndex], ...prev]);
        setUpdateIndex(prev => prev + 1);
      } else {
        clearInterval(interval);
      }
    }, 5000); // New commentary every 5 seconds for demo

    return () => clearInterval(interval);
  }, [updateIndex]);

  const getIcon = (type: Commentary['type']) => {
    switch (type) {
      case 'goal': return <Goal size={16} className="text-yellow-500" />;
      case 'card': return <div className="w-3 h-4 bg-yellow-500 rounded-sm"></div>;
      case 'corner': return <Flag size={16} className="text-zinc-400" />;
      case 'foul': return <AlertCircle size={16} className="text-red-400" />;
      case 'attack': return <Activity size={16} className="text-blue-400" />;
      default: return <Clock size={16} className="text-zinc-500" />;
    }
  };

  const getBorderColor = (team?: 'home' | 'away') => {
    if (team === 'home') return 'border-r-yellow-500';
    if (team === 'away') return 'border-r-zinc-500';
    return 'border-r-transparent';
  };

  return (
    <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-4 shadow-sm animate-in fade-in slide-in-from-right-4 flex flex-col h-[400px]">
      <div className="flex items-center justify-between mb-4 pb-3 border-b border-zinc-800/50 flex-shrink-0">
        <h3 className="font-bold text-white text-sm flex items-center gap-2">
          <Activity size={16} className="text-red-500 animate-pulse" />
          تغطية مباشرة
        </h3>
        <span className="text-[10px] text-zinc-500 font-bold bg-zinc-800 px-2 py-1 rounded">
          {updateIndex < mockUpdates.length ? 'جاري التحديث...' : 'انتهت'}
        </span>
      </div>

      <div 
        ref={containerRef}
        className="flex-1 overflow-y-auto space-y-3 pr-2 scrollbar-thin scrollbar-thumb-zinc-800 scrollbar-track-transparent"
        style={{ direction: 'rtl' }}
      >
        {commentaries.map((item, i) => (
          <div 
            key={item.id} 
            className={`bg-zinc-800/30 p-3 rounded-lg border-r-4 ${getBorderColor(item.team)} ${i === 0 ? 'animate-in fade-in slide-in-from-top-2 bg-zinc-800/80 border-t border-b border-l border-zinc-700/50 shadow-md' : ''} transition-all duration-500`}
          >
            <div className="flex items-start gap-3">
              <div className="flex flex-col items-center gap-1 min-w-[40px] pt-1 shrink-0">
                <span className="text-xs font-black text-white">{item.minute}'</span>
                {getIcon(item.type)}
              </div>
              <p className={`text-sm leading-relaxed ${item.type === 'goal' ? 'font-bold text-yellow-500' : 'text-zinc-300'}`}>
                {item.text}
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
