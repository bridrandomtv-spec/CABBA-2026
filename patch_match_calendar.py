import re

with open("src/components/MatchCalendar.tsx", "r") as f:
    content = f.read()

import_search = "import { Calendar, ChevronLeft, ChevronRight, Heart, CalendarPlus, Bell, MapPin } from 'lucide-react';\nimport { useFavorites } from '../hooks/useFavorites';"
import_replace = "import { Calendar, ChevronLeft, ChevronRight, Heart, CalendarPlus, Bell, MapPin } from 'lucide-react';\nimport { useFavorites } from '../hooks/useFavorites';\nimport { useState, useEffect } from 'react';\nimport { collection, query, orderBy, onSnapshot } from 'firebase/firestore';\nimport { db } from '../lib/firebase';\nimport { Match } from '../types';"
content = content.replace(import_search, import_replace)

data_search = """export const MATCHES_DATA = [
  { id: '1', date: '24 أكتوبر 2026', time: '18:00', opponent: 'وفاق سطيف', location: 'برج بوعريريج', type: 'الرابطة 1', status: 'upcoming', day: 24, score: null },
  { id: '2', date: '30 أكتوبر 2026', time: '16:00', opponent: 'مولودية الجزائر', location: 'الجزائر العاصمة', type: 'الرابطة 1', status: 'upcoming', day: 30, score: null },
  { id: '3', date: '12 أكتوبر 2026', time: '15:00', opponent: 'شبيبة القبائل', location: 'برج بوعريريج', type: 'الرابطة 1', status: 'past', day: 12, score: '2-1' },
  { id: '4', date: '5 أكتوبر 2026', time: '16:00', opponent: 'شباب قسنطينة', location: 'قسنطينة', type: 'الرابطة 1', status: 'past', day: 5, score: '0-0' },
];

export default function MatchCalendar() {"""

data_replace = """export default function MatchCalendar() {"""
content = content.replace(data_search, data_replace)

logic_search = """  const [currentMonthIndex, setCurrentMonthIndex] = useState(2); // October (index 2 for display)
  const [filterStatus, setFilterStatus] = useState<'all' | 'upcoming' | 'past'>('all');
  
  const { favorites, toggleFavorite } = useFavorites();

  const prevMonth = () => setCurrentMonthIndex(prev => Math.max(0, prev - 1));
  const nextMonth = () => setCurrentMonthIndex(prev => Math.min(months.length - 1, prev + 1));

  const matches = MATCHES_DATA;"""
  
logic_replace = """  const [currentMonthIndex, setCurrentMonthIndex] = useState(2); // October (index 2 for display)
  const [filterStatus, setFilterStatus] = useState<'all' | 'upcoming' | 'past'>('all');
  const [matches, setMatches] = useState<Match[]>([]);
  
  const { favorites, toggleFavorite } = useFavorites();

  useEffect(() => {
    const q = query(collection(db, 'matches'), orderBy('createdAt', 'desc'));
    const un = onSnapshot(q, (snapshot) => {
      const data: Match[] = [];
      snapshot.forEach(doc => data.push({ id: doc.id, ...doc.data() } as Match));
      setMatches(data);
    });
    return () => un();
  }, []);

  const prevMonth = () => setCurrentMonthIndex(prev => Math.max(0, prev - 1));
  const nextMonth = () => setCurrentMonthIndex(prev => Math.min(months.length - 1, prev + 1));
"""
content = content.replace(logic_search, logic_replace)

filtered_search = """  const filteredMatches = matches.filter(m => {
    if (filterStatus === 'all') return true;
    return m.status === filterStatus;
  });"""

filtered_replace = """  const filteredMatches = matches.filter(m => {
    if (filterStatus === 'all') return true;
    if (filterStatus === 'upcoming') return m.status === 'scheduled';
    if (filterStatus === 'past') return m.status === 'finished';
    return true;
  });"""
content = content.replace(filtered_search, filtered_replace)

day_render_search = """      const matchOnDay = filteredMatches.find(m => m.day === day);"""
day_render_replace = """      const matchOnDay = filteredMatches.find(m => {
        // Just extract day from m.date string if possible, or skip for now
        // This is a rough hack to map text date to day number
        const matchDay = parseInt(m.date.split(' ')[0]) || 0;
        return matchDay === day;
      });"""
content = content.replace(day_render_search, day_render_replace)

match_card_search = """                  <div className="flex justify-between items-center pb-3 border-b border-zinc-800/50">
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
                        <button onClick={() => alert('هذه الخاصية ستتوفر قريباً!')} className="text-[10px] font-bold text-yellow-500 flex items-center gap-1 bg-yellow-500/10 px-2 py-1 rounded-md hover:bg-yellow-500 hover:text-black transition-colors">
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
                </div>"""
                
match_card_replace = """                  <div className="flex justify-between items-center pb-3 border-b border-zinc-800/50">
                  <div className="flex items-center gap-2">
                    <button 
                      onClick={() => toggleFavorite(match.id)}
                      className={`transition-colors ${favorites.includes(match.id) ? 'text-red-500' : 'text-zinc-600 hover:text-red-400'}`}
                    >
                      <Heart size={16} className={favorites.includes(match.id) ? 'fill-current' : ''} />
                    </button>
                    <span className="text-[10px] font-bold text-zinc-500 bg-zinc-800 px-2 py-1 rounded">{match.competition}</span>
                  </div>
                  <div className="flex items-center gap-1.5 text-xs font-bold text-zinc-400">
                    <Calendar size={12} />
                    <span>{match.date}</span>
                  </div>
                </div>
                
                <div className="flex justify-between items-center">
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 bg-zinc-800 rounded-full flex items-center justify-center border-2 border-zinc-700">
                      <span className="font-bold text-xs text-white truncate max-w-[20px]">{match.awayTeam.charAt(0)}</span>
                    </div>
                    <div>
                      <h4 className="font-bold text-white text-sm">{match.awayTeam}</h4>
                      <div className="flex items-center gap-1 text-[10px] text-zinc-500 mt-0.5">
                        <MapPin size={10} /> {match.stadium}
                      </div>
                    </div>
                  </div>
                  
                  {match.status === 'scheduled' ? (
                    <div className="flex flex-col items-center gap-2">
                      <span className="font-black text-lg text-white">{match.time}</span>
                      <div className="flex gap-2">
                        <button onClick={() => alert('هذه الخاصية ستتوفر قريباً!')} className="text-[10px] font-bold text-yellow-500 flex items-center gap-1 bg-yellow-500/10 px-2 py-1 rounded-md hover:bg-yellow-500 hover:text-black transition-colors">
                          <Bell size={12} /> تذكير
                        </button>
                        <button 
                          onClick={() => addToCalendar(match as any)}
                          className="text-[10px] font-bold text-blue-500 flex items-center gap-1 bg-blue-500/10 px-2 py-1 rounded-md hover:bg-blue-500 hover:text-zinc-50 transition-colors"
                        >
                          <CalendarPlus size={12} /> تقويم
                        </button>
                      </div>
                    </div>
                  ) : (
                    <div className="flex flex-col items-center gap-1">
                      <span className="text-[10px] text-zinc-500 font-bold">انتهت</span>
                      <span className="font-black text-xl text-white tracking-widest">{match.homeScore}-{match.awayScore}</span>
                    </div>
                  )}
                </div>"""
content = content.replace(match_card_search, match_card_replace)

with open("src/components/MatchCalendar.tsx", "w") as f:
    f.write(content)

