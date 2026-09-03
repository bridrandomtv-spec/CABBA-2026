import { useState } from 'react';
import MatchPredictions from './MatchPredictions';
import MatchMVP from './MatchMVP';
import MatchScout from './MatchScout';
import { Target } from 'lucide-react';

import { Activity, Users, Star, BarChart3, TrendingUp, Bus, MapPin, CheckCircle, Calendar, Bell, Ticket, CalendarPlus, History } from 'lucide-react';
import TicketManager from './TicketManager';
import InGameNotifications from './InGameNotifications';
import LiveMatchUpdate from './LiveMatchUpdate';

import MatchHighlights from './MatchHighlights';
import MatchStatsVisualization from './MatchStatsVisualization';
import SeasonStats from './SeasonStats';
import PlayerComparison from './PlayerComparison';
import { GitCompare } from 'lucide-react';
import { PieChart as PieChartIcon } from 'lucide-react';
import MatchCalendar from './MatchCalendar';
import MatchAbsences from './MatchAbsences';
import MatchArchive from './MatchArchive';

export default function MatchCenter() {
  const [activeTab, setActiveTab] = useState<'live' | 'stats' | 'season' | 'compare' | 'formation' | 'motm' | 'travel' | 'predictions' | 'calendar' | 'tickets' | 'scout' | 'archive'>('live');
  const [cabbaScore, setCabbaScore] = useState(0);
  const [opponentScore, setOpponentScore] = useState(0);
  const [predicted, setPredicted] = useState(false);

  const addToCalendar = (match: any) => {
    const icsContent = `BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
SUMMARY:الكابا ضد ${match.opponent}
DESCRIPTION:مباراة ضمن ${match.type}
LOCATION:${match.location}
END:VEVENT
END:VCALENDAR`;
    const blob = new Blob([icsContent], { type: 'text/calendar;charset=utf-8' });
    const link = document.createElement('a');
    link.href = window.URL.createObjectURL(blob);
    link.setAttribute('download', `match-${match.id}.ics`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div className="p-4 space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-500" dir="rtl">
      
      {/* Match Header */}
      <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-4 text-center shadow-lg">
        <span className="text-red-500 font-bold text-xs uppercase tracking-wider mb-2 block animate-pulse">مباشر - الشوط الثاني</span>
        <div className="flex justify-between items-center px-4">
          <div className="flex flex-col items-center">
            <div className="w-10 h-10 bg-black rounded-full flex items-center justify-center border-2 border-yellow-500 shadow-[0_0_10px_rgba(234,179,8,0.3)]">
              <span className="font-bold text-yellow-500">C</span>
            </div>
            <span className="font-bold text-xs text-white mt-1">الكابا</span>
          </div>
          
          <div className="flex flex-col items-center">
            <span className="text-3xl font-black text-white tracking-widest">1 - 0</span>
            <span className="text-xs text-zinc-400 mt-1">68'</span>
          </div>
          
          <div className="flex flex-col items-center">
            <div className="w-10 h-10 rounded-full flex items-center justify-center border-2 border-zinc-700" style={{ backgroundColor: "#ffffff" }}>
              <span className="font-bold text-black">M</span>
            </div>
            <span className="font-bold text-xs text-white mt-1">المنافس</span>
          </div>
        </div>
      </div>

      {/* Tabs */}
      <div className="flex bg-zinc-900 p-1 rounded-xl border border-zinc-800 overflow-x-auto scrollbar-hide">
        <button 
          onClick={() => setActiveTab('live')}
          className={`flex-none px-4 flex justify-center items-center gap-2 py-2 text-xs font-bold rounded-lg transition-colors ${activeTab === 'live' ? 'bg-zinc-800 text-yellow-500 shadow-sm' : 'text-zinc-500'}`}
        >
          <Activity size={14} /> مباشر
        </button>
        <button 
          onClick={() => setActiveTab('stats')}
          className={`flex-none px-4 flex justify-center items-center gap-2 py-2 text-xs font-bold rounded-lg transition-colors ${activeTab === 'stats' ? 'bg-zinc-800 text-yellow-500 shadow-sm' : 'text-zinc-500'}`}
        >
          <BarChart3 size={14} /> الإحصائيات
        </button>
        <button 
          onClick={() => setActiveTab('season')}
          className={`flex-none px-4 flex justify-center items-center gap-2 py-2 text-xs font-bold rounded-lg transition-colors ${activeTab === 'season' ? 'bg-zinc-800 text-yellow-500 shadow-sm' : 'text-zinc-500'}`}
        >
          <PieChartIcon size={14} /> إحصائيات الموسم
        </button>
        <button 
          onClick={() => setActiveTab('formation')}
          className={`flex-none px-4 flex justify-center items-center gap-2 py-2 text-xs font-bold rounded-lg transition-colors ${activeTab === 'formation' ? 'bg-zinc-800 text-yellow-500 shadow-sm' : 'text-zinc-500'}`}
        >
          <Users size={14} /> التشكيلة
        </button>
        <button 
          onClick={() => setActiveTab('motm')}
          className={`flex-none px-4 flex justify-center items-center gap-2 py-2 text-xs font-bold rounded-lg transition-colors ${activeTab === 'motm' ? 'bg-zinc-800 text-yellow-500 shadow-sm' : 'text-zinc-500'}`}
        >
          <Star size={14} /> رجل المباراة
        </button>
        <button 
          onClick={() => setActiveTab('predictions')}
          className={`flex-none px-4 flex justify-center items-center gap-2 py-2 text-xs font-bold rounded-lg transition-colors ${activeTab === 'predictions' ? 'bg-zinc-800 text-yellow-500 shadow-sm' : 'text-zinc-500'}`}
        >
          <TrendingUp size={14} /> التوقعات
        </button>
        <button 
          onClick={() => setActiveTab('travel')}
          className={`flex-none px-4 flex justify-center items-center gap-2 py-2 text-xs font-bold rounded-lg transition-colors ${activeTab === 'travel' ? 'bg-zinc-800 text-yellow-500 shadow-sm' : 'text-zinc-500'}`}
        >
          <Bus size={14} /> التنقلات
        </button>
        <button 
          onClick={() => setActiveTab('calendar')}
          className={`flex-none px-4 flex justify-center items-center gap-2 py-2 text-xs font-bold rounded-lg transition-colors ${activeTab === 'calendar' ? 'bg-zinc-800 text-yellow-500 shadow-sm' : 'text-zinc-500'}`}
        >
          <Calendar size={14} /> التقويم
        </button>
        <button 
          onClick={() => setActiveTab('tickets')}
          className={`flex-none px-4 flex justify-center items-center gap-2 py-2 text-xs font-bold rounded-lg transition-colors ${activeTab === 'tickets' ? 'bg-zinc-800 text-yellow-500 shadow-sm' : 'text-zinc-500'}`}
        >
          <Ticket size={14} /> التذاكر
        </button>
        <button 
          onClick={() => setActiveTab('compare')}
          className={`flex-none px-4 flex justify-center items-center gap-2 py-2 text-xs font-bold rounded-lg transition-colors ${activeTab === 'compare' ? 'bg-zinc-800 text-yellow-500 shadow-sm' : 'text-zinc-500'}`}
        >
          <GitCompare size={14} /> مقارنة اللاعبين
        </button>
        <button 
          onClick={() => setActiveTab('scout')}
          className={`flex-none px-4 flex justify-center items-center gap-2 py-2 text-xs font-bold rounded-lg transition-colors ${activeTab === 'scout' ? 'bg-zinc-800 text-yellow-500 shadow-sm' : 'text-zinc-500'}`}
        >
          <Target size={14} /> كشاف المباراة
        </button>
        <button 
          onClick={() => setActiveTab('archive')}
          className={`flex-none px-4 flex justify-center items-center gap-2 py-2 text-xs font-bold rounded-lg transition-colors ${activeTab === 'archive' ? 'bg-zinc-800 text-yellow-500 shadow-sm' : 'text-zinc-500'}`}
        >
          <History size={14} /> الأرشيف
        </button>
      </div>

      {/* Content */}
      {activeTab === 'live' && (
        <>
          <InGameNotifications />
          <LiveMatchUpdate />
          <MatchHighlights />
        </>
      )}

      {activeTab === 'stats' && (
        <div className="space-y-4 animate-in fade-in slide-in-from-right-4">
          <MatchStatsVisualization />
          
          <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-4">
            <h3 className="font-bold text-sm text-white mb-4 text-center">الاستحواذ على الكرة</h3>
            <div className="flex justify-between text-xs font-bold text-white mb-2">
              <span>الكابا 58%</span>
              <span>المنافس 42%</span>
            </div>
            <div className="w-full h-3 bg-zinc-800 rounded-full overflow-hidden flex">
              <div className="h-full bg-yellow-500 w-[58%]"></div>
              <div className="h-full bg-zinc-600 w-[42%]"></div>
            </div>
          </div>
          
          <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-4 space-y-4">
            <StatRow label="التسديدات (على المرمى)" val1="12 (5)" val2="8 (2)" leftColor="bg-yellow-500" rightColor="bg-zinc-600" leftPercent={60} rightPercent={40} />
            <StatRow label="التمريرات الدقيقة" val1="340" val2="210" leftColor="bg-yellow-500" rightColor="bg-zinc-600" leftPercent={62} rightPercent={38} />
            <StatRow label="الركنيات" val1="6" val2="2" leftColor="bg-yellow-500" rightColor="bg-zinc-600" leftPercent={75} rightPercent={25} />
            <StatRow label="البطاقات الصفراء" val1="1" val2="3" leftColor="bg-yellow-500" rightColor="bg-zinc-600" leftPercent={25} rightPercent={75} />
          </div>
        </div>
      )}
      {activeTab === 'season' && <SeasonStats />}
      {activeTab === 'compare' && <PlayerComparison />}

      {activeTab === 'formation' && (
        <div className="animate-in fade-in slide-in-from-right-4">
          <div className="relative w-full aspect-[2/3] bg-emerald-900/40 border-2 border-emerald-900/80 rounded-xl overflow-hidden flex items-center justify-center p-2 shadow-inner">
            {/* Field Lines */}
            <div className="absolute inset-0 border-[1px] border-emerald-500/30 m-4 rounded"></div>
            <div className="absolute top-1/2 left-4 right-4 h-[1px] bg-emerald-500/30"></div>
            <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-16 h-16 border-[1px] border-emerald-500/30 rounded-full"></div>
            <div className="absolute top-4 left-1/2 -translate-x-1/2 w-32 h-16 border-[1px] border-emerald-500/30 border-t-0 rounded-b-sm"></div>
            <div className="absolute bottom-4 left-1/2 -translate-x-1/2 w-32 h-16 border-[1px] border-emerald-500/30 border-b-0 rounded-t-sm"></div>
            
            {/* Players (4-3-3 simplified) */}
            <div className="absolute w-full h-full p-4 flex flex-col justify-between py-8">
              {/* Attackers */}
              <div className="flex justify-between px-8">
                <PlayerNode number="11" name="جناح" />
                <PlayerNode number="9" name="مهاجم" />
                <PlayerNode number="7" name="جناح" />
              </div>
              {/* Midfielders */}
              <div className="flex justify-around px-8 mt-2">
                <PlayerNode number="8" name="وسط" />
                <PlayerNode number="6" name="ارتكاز" />
                <PlayerNode number="10" name="صانع" />
              </div>
              {/* Defenders */}
              <div className="flex justify-between px-2 mt-4">
                <PlayerNode number="3" name="ظ.أيسر" />
                <PlayerNode number="5" name="مدافع" />
                <PlayerNode number="4" name="مدافع" />
                <PlayerNode number="2" name="ظ.أيمن" />
              </div>
              {/* Goalkeeper */}
              <div className="flex justify-center mt-2">
                <PlayerNode number="1" name="حارس" />
              </div>
            </div>
          </div>
          <MatchAbsences />
        </div>
      )}

      {activeTab === 'motm' && <MatchMVP />}

      {activeTab === 'predictions' && <MatchPredictions />}

      {activeTab === 'travel' && (
        <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-5 animate-in fade-in slide-in-from-right-4">
          <div className="flex items-center gap-3 mb-6">
            <div className="w-12 h-12 bg-yellow-500/10 rounded-full flex items-center justify-center text-yellow-500">
              <Bus size={24} />
            </div>
            <div>
              <h3 className="font-bold text-white text-lg">تنقل الجراد الأصفر</h3>
              <p className="text-xs text-zinc-400">نحو ملعب 5 جويلية (الجزائر العاصمة)</p>
            </div>
          </div>
          
          <div className="space-y-4 relative before:absolute before:inset-0 before:ml-5 before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-transparent before:via-zinc-800 before:to-transparent">
            
            <div className="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
              <div className="flex items-center justify-center w-10 h-10 rounded-full border border-yellow-500 bg-zinc-900 text-yellow-500 shadow-[0_0_10px_rgba(234,179,8,0.3)] shrink-0 z-10">
                <MapPin size={16} />
              </div>
              <div className="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] p-4 rounded-xl border border-yellow-500/30 bg-zinc-800/50">
                <div className="flex justify-between items-center mb-1">
                  <h4 className="font-bold text-white text-sm">نقطة التجمع (ساحة القلعة)</h4>
                  <span className="text-xs text-yellow-500 font-bold">06:00 ص</span>
                </div>
                <p className="text-xs text-zinc-400">يرجى الحضور باكراً لتنظيم الحافلات واستلام التذاكر الرقمية.</p>
              </div>
            </div>

            <div className="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group">
              <div className="flex items-center justify-center w-10 h-10 rounded-full border border-zinc-700 bg-zinc-900 text-zinc-500 shrink-0 z-10">
                <Bus size={16} />
              </div>
              <div className="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] p-4 rounded-xl border border-zinc-800 bg-zinc-900">
                <div className="flex justify-between items-center mb-1">
                  <h4 className="font-bold text-white text-sm">الانطلاق</h4>
                  <span className="text-xs text-zinc-500 font-bold">07:00 ص</span>
                </div>
                <p className="text-xs text-zinc-500">انطلاق القافلة نحو العاصمة تحت حراسة أمنية.</p>
              </div>
            </div>

            <div className="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group">
              <div className="flex items-center justify-center w-10 h-10 rounded-full border border-zinc-700 bg-zinc-900 text-zinc-500 shrink-0 z-10">
                <CheckCircle size={16} />
              </div>
              <div className="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] p-4 rounded-xl border border-zinc-800 bg-zinc-900">
                <div className="flex justify-between items-center mb-1">
                  <h4 className="font-bold text-white text-sm">الدخول للملعب</h4>
                  <span className="text-xs text-zinc-500 font-bold">14:00 م</span>
                </div>
                <p className="text-xs text-zinc-500">تسهيل الدخول عبر بوابات مخصصة بفضل التذاكر الرقمية المسبقة.</p>
              </div>
            </div>
            
          </div>

          <button onClick={() => alert('هذه الخاصية ستتوفر قريباً!')} className="w-full mt-6 bg-zinc-800 border border-yellow-500/50 hover:bg-zinc-700 text-yellow-500 text-sm font-bold py-3 rounded-xl transition-colors flex items-center justify-center gap-2">
             احجز مكانك في الحافلة (250 دج)
          </button>
        </div>
      )}

      {activeTab === 'calendar' && <MatchCalendar />}

      {activeTab === 'tickets' && <TicketManager />}
      {activeTab === 'scout' && <MatchScout />}
      {activeTab === 'archive' && <MatchArchive />}
    </div>
  );
}

function StatRow({ label, val1, val2, leftPercent, rightPercent, leftColor, rightColor }: any) {
  return (
    <div className="space-y-2">
      <div className="flex justify-between text-[11px] font-bold text-white">
        <span>{val1}</span>
        <span className="text-zinc-400">{label}</span>
        <span>{val2}</span>
      </div>
      <div className="flex h-1.5 bg-zinc-800 rounded-full overflow-hidden gap-1">
        <div className={`h-full rounded-full ${leftColor}`} style={{ width: `${leftPercent}%` }}></div>
        <div className={`h-full rounded-full ${rightColor}`} style={{ width: `${rightPercent}%` }}></div>
      </div>
    </div>
  );
}

function PlayerNode({ number, name }: { number: string, name: string }) {
  return (
    <div className="flex flex-col items-center z-10 hover:scale-110 transition-transform cursor-pointer">
      <div className="w-8 h-8 rounded-full bg-yellow-500 border-[3px] border-zinc-900 flex items-center justify-center font-black text-zinc-900 text-xs shadow-md">
        {number}
      </div>
      <span className="text-[9px] font-bold text-white bg-zinc-900/80 backdrop-blur-sm px-1.5 py-0.5 rounded-full mt-1 border border-zinc-700/50">{name}</span>
    </div>
  );
}
