import { useState } from 'react';
import { Calendar, MapPin, Bell, CalendarPlus, ChevronRight, ChevronLeft, Heart, Filter } from 'lucide-react';
import { useFavorites } from '../hooks/useFavorites';

export const MATCHES_DATA = [
  { id: 1, date: '15 فيفري', day: 15, time: '14:30', opponent: 'مولودية وهران', type: 'الرابطة المحترفة الأولى', location: 'ملعب 20 أوت', status: 'past', score: '2 - 0', month: 1 },
  { id: 2, date: '25 فيفري', day: 25, time: '16:00', opponent: 'شباب بلوزداد', type: 'الرابطة المحترفة الأولى', location: 'ملعب 20 أوت 1955', status: 'past', score: '1 - 1', month: 1 },
  { id: 3, date: '05 مارس', day: 5, time: '15:00', opponent: 'شبيبة القبائل', type: 'الرابطة المحترفة الأولى', location: 'ملعب 1 نوفمبر', status: 'past', score: '1 - 2', month: 2 },
  { id: 4, date: '15 مارس', day: 15, time: '14:30', opponent: 'مولودية الجزائر', type: 'الرابطة المحترفة الأولى', location: 'ملعب 5 جويلية', status: 'upcoming', month: 2 },
  { id: 5, date: '22 مارس', day: 22, time: '16:00', opponent: 'وفاق سطيف', type: 'الرابطة المحترفة الأولى', location: 'ملعب 20 أوت', status: 'upcoming', month: 2 },
  { id: 6, date: '04 أفريل', day: 4, time: '15:00', opponent: 'اتحاد العاصمة', type: 'الرابطة المحترفة الأولى', location: 'ملعب عمر حمادي', status: 'upcoming', month: 3 },
  { id: 7, date: '18 أفريل', day: 18, time: '16:00', opponent: 'نجم مقرة', type: 'الرابطة المحترفة الأولى', location: 'ملعب 20 أوت', status: 'upcoming', month: 3 },
];

export default function MatchCalendar() {
  const [currentMonthIndex, setCurrentMonthIndex] = useState(2); // Default to March (index 2 for Jan, Feb, Mar)
  const [filterStatus, setFilterStatus] = useState<'all' | 'past' | 'upcoming'>('all');
  const { favorites, toggleFavorite } = useFavorites();

  
  const months = ['جانفي', 'فيفري', 'مارس', 'أفريل', 'ماي', 'جوان'];
  
  // Fake year to get proper days, say 2024 (leap year)
  const monthDays = [31, 29, 31, 30, 31, 30];
  const startDayOfWeek = [1, 4, 5, 1, 3, 6]; // just fake starting day of week for the grid (0=Sunday, 6=Saturday)
  
  const matches = MATCHES_DATA;

  const filteredMatches = matches.filter(m => m.month === currentMonthIndex && (filterStatus === 'all' || m.status === filterStatus));
  
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

  const nextMonth = () => {
    if (currentMonthIndex < months.length - 1) {
      setCurrentMonthIndex(prev => prev + 1);
    }
  };

  const prevMonth = () => {
    if (currentMonthIndex > 0) {
      setCurrentMonthIndex(prev => prev - 1);
    }
  };

  const renderCalendarGrid = () => {
    const days = monthDays[currentMonthIndex];
    const startDay = startDayOfWeek[currentMonthIndex];
    const grid = [];
    
    // Weekday headers
    const weekDays = ['أحد', 'إثنين', 'ثلاثاء', 'أربعاء', 'خميس', 'جمعة', 'سبت'];
    const headers = weekDays.map((d, i) => (
      <div key={`header-${i}`} className="text-center text-[10px] text-zinc-500 font-bold py-1">
        {d}
      </div>
    ));
    
    // Empty cells before start day
    for (let i = 0; i < startDay; i++) {
      grid.push(<div key={`empty-${i}`} className="p-2"></div>);
    }
    
    // Day cells
    for (let day = 1; day <= days; day++) {
      const matchOnDay = filteredMatches.find(m => m.day === day);
      const isToday = day === 12 && currentMonthIndex === 2; // fake today
      
      grid.push(
        <div 
          key={`day-${day}`} 
          className={`flex flex-col items-center justify-center p-1.5 aspect-square rounded-lg border transition-colors ${
            matchOnDay 
              ? 'border-yellow-500/50 bg-yellow-500/10 cursor-pointer hover:bg-yellow-500/20' 
              : isToday
                ? 'border-zinc-500 bg-zinc-800'
                : 'border-transparent hover:bg-zinc-800/50'
          }`}
        >
          <span className={`text-xs font-bold ${matchOnDay ? 'text-yellow-500' : isToday ? 'text-white' : 'text-zinc-400'}`}>
            {day}
          </span>
          {matchOnDay && (
            <div className="w-1.5 h-1.5 rounded-full bg-yellow-500 mt-1"></div>
          )}
        </div>
      );
    }
    
    return (
      <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-4 mb-6 shadow-sm">
        <div className="grid grid-cols-7 gap-1 mb-2">
          {headers}
        </div>
        <div className="grid grid-cols-7 gap-1">
          {grid}
        </div>
        <div className="flex justify-center gap-4 mt-4 pt-4 border-t border-zinc-800/50 text-[10px] text-zinc-400">
          <div className="flex items-center gap-1.5">
            <div className="w-2 h-2 rounded-full bg-yellow-500"></div>
            <span>يوم المباراة</span>
          </div>
          <div className="flex items-center gap-1.5">
            <div className="w-2 h-2 rounded-full bg-zinc-500"></div>
            <span>اليوم</span>
          </div>
        </div>
      </div>
    );
  };

  return (
    <div className="space-y-4 animate-in fade-in slide-in-from-right-4">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <h3 className="font-bold text-white text-lg flex items-center gap-2">
            <Calendar className="text-yellow-500" size={20} />
            التقويم
          </h3>
          <div className="flex bg-zinc-800 rounded-lg p-1 text-[10px] font-bold">
            <button 
              onClick={() => setFilterStatus('all')} 
              className={`px-2 py-1 rounded-md transition-colors ${filterStatus === 'all' ? 'bg-zinc-700 text-white' : 'text-zinc-400 hover:text-zinc-300'}`}
            >الكل</button>
            <button 
              onClick={() => setFilterStatus('upcoming')} 
              className={`px-2 py-1 rounded-md transition-colors ${filterStatus === 'upcoming' ? 'bg-yellow-500 text-black' : 'text-zinc-400 hover:text-zinc-300'}`}
            >القادمة</button>
            <button 
              onClick={() => setFilterStatus('past')} 
              className={`px-2 py-1 rounded-md transition-colors ${filterStatus === 'past' ? 'bg-zinc-700 text-white' : 'text-zinc-400 hover:text-zinc-300'}`}
            >السابقة</button>
          </div>
        </div>
        
        <div className="flex items-center gap-3 bg-zinc-900 border border-zinc-800 rounded-full px-3 py-1">
            <button onClick={prevMonth} disabled={currentMonthIndex === 0} className={`p-1 rounded-full hover:bg-zinc-800 transition-colors ${currentMonthIndex === 0 ? 'text-zinc-700' : 'text-zinc-400 hover:text-white'}`}>
                <ChevronRight size={16} />
            </button>
            <span className="text-sm font-bold text-yellow-500 min-w-[60px] text-center">{months[currentMonthIndex]}</span>
            <button onClick={nextMonth} disabled={currentMonthIndex === months.length - 1} className={`p-1 rounded-full hover:bg-zinc-800 transition-colors ${currentMonthIndex === months.length - 1 ? 'text-zinc-700' : 'text-zinc-400 hover:text-white'}`}>
                <ChevronLeft size={16} />
            </button>
        </div>
      </div>
      
      {renderCalendarGrid()}
      
      <div className="space-y-3">
        <h4 className="font-bold text-zinc-400 text-sm mb-2 px-2">مباريات الشهر</h4>
        {filteredMatches.length > 0 ? (
            filteredMatches.map(match => (
              <div key={match.id} className="bg-zinc-900 border border-zinc-800 rounded-xl p-4 shadow-sm flex flex-col gap-3 transition-all hover:border-zinc-700">
                <div className="flex justify-between items-center pb-3 border-b border-zinc-800/50">
                  <div className="flex items-center gap-2">
                    <button 
                      onClick={() => toggleFavorite(match.id)}
                      className={`transition-colors ${favorites.includes(match.id) ? 'text-red-500' : 'text-zinc-600 hover:text-red-400'}`}
                    >
                      <Heart size={16} className={favorites.includes(match.id) ? 'fill-current' : ''} />
                    </button>
                    <span className="text-[10px] font-bold text-zinc-500 bg-zinc-800 px-2 py-1 rounded">{match.type}</span>
                  </div>
                  <div className="flex items-center gap-1.5 text-xs font-bold text-zinc-400">
                    <Calendar size={12} />
                    <span>{match.date}</span>
                  </div>
                </div>
                
                <div className="flex justify-between items-center">
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 bg-zinc-800 rounded-full flex items-center justify-center border-2 border-zinc-700">
                      <span className="font-bold text-xs text-white truncate max-w-[20px]">{match.opponent.charAt(0)}</span>
                    </div>
                    <div>
                      <h4 className="font-bold text-white text-sm">{match.opponent}</h4>
                      <div className="flex items-center gap-1 text-[10px] text-zinc-500 mt-0.5">
                        <MapPin size={10} /> {match.location}
                      </div>
                    </div>
                  </div>
                  
                  {match.status === 'upcoming' ? (
                    <div className="flex flex-col items-center gap-2">
                      <span className="font-black text-lg text-white">{match.time}</span>
                      <div className="flex gap-2">
                        <button className="text-[10px] font-bold text-yellow-500 flex items-center gap-1 bg-yellow-500/10 px-2 py-1 rounded-md hover:bg-yellow-500 hover:text-black transition-colors">
                          <Bell size={12} /> تذكير
                        </button>
                        <button 
                          onClick={() => addToCalendar(match)}
                          className="text-[10px] font-bold text-blue-500 flex items-center gap-1 bg-blue-500/10 px-2 py-1 rounded-md hover:bg-blue-500 hover:text-zinc-50 transition-colors"
                        >
                          <CalendarPlus size={12} /> تقويم
                        </button>
                      </div>
                    </div>
                  ) : (
                    <div className="flex flex-col items-center gap-1">
                      <span className="text-[10px] text-zinc-500 font-bold">انتهت</span>
                      <span className="font-black text-xl text-white tracking-widest">{match.score}</span>
                    </div>
                  )}
                </div>
              </div>
            ))
        ) : (
            <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-8 flex flex-col items-center justify-center text-center">
                <Calendar size={48} className="text-zinc-700 mb-4" />
                <h4 className="font-bold text-zinc-400">لا توجد مباريات</h4>
                <p className="text-xs text-zinc-500 mt-2">لا توجد مباريات مبرمجة في هذا الشهر</p>
            </div>
        )}
      </div>
    </div>
  );
}
