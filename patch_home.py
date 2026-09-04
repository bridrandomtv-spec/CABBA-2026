import re

with open("src/components/Home.tsx", "r") as f:
    content = f.read()

import_search = "import { Tab } from '../types';"
import_replace = "import { Tab, NewsItem, Match } from '../types';\nimport { useState, useEffect } from 'react';\nimport { collection, query, orderBy, limit, onSnapshot, where } from 'firebase/firestore';\nimport { db } from '../lib/firebase';"
content = content.replace(import_search, import_replace)

body_search = """export default function Home({ onNavigate }: HomeProps) {
  return (
    <div className="w-full animate-in fade-in" dir="rtl">"""

body_replace = """export default function Home({ onNavigate }: HomeProps) {
  const [latestNews, setLatestNews] = useState<NewsItem[]>([]);
  const [upcomingMatches, setUpcomingMatches] = useState<Match[]>([]);
  const [latestResult, setLatestResult] = useState<Match | null>(null);

  useEffect(() => {
    // Fetch News
    const qNews = query(collection(db, 'news'), orderBy('createdAt', 'desc'), limit(3));
    const unNews = onSnapshot(qNews, (snapshot) => {
      const data: NewsItem[] = [];
      snapshot.forEach(doc => data.push({ id: doc.id, ...doc.data() } as NewsItem));
      setLatestNews(data);
    });

    // Fetch Matches (Upcoming)
    const qUpcoming = query(
      collection(db, 'matches'), 
      where('status', 'in', ['scheduled', 'live']), 
      limit(2) // Needs a composite index if ordered by date, doing simple fetch for now
    );
    const unUpcoming = onSnapshot(qUpcoming, (snapshot) => {
      const data: Match[] = [];
      snapshot.forEach(doc => data.push({ id: doc.id, ...doc.data() } as Match));
      // Local sort to avoid requiring complex composite index initially
      data.sort((a, b) => b.createdAt - a.createdAt);
      setUpcomingMatches(data);
    });

    // Fetch Latest Result
    const qResult = query(
      collection(db, 'matches'), 
      where('status', '==', 'finished'),
      limit(1)
    );
    const unResult = onSnapshot(qResult, (snapshot) => {
      if (!snapshot.empty) {
        setLatestResult({ id: snapshot.docs[0].id, ...snapshot.docs[0].data() } as Match);
      }
    });

    return () => { unNews(); unUpcoming(); unResult(); };
  }, []);

  return (
    <div className="w-full animate-in fade-in pb-20" dir="rtl">"""
content = content.replace(body_search, body_replace)

news_ui_search = """        <div className="flex gap-4 overflow-x-auto pb-4 snap-x hide-scrollbar">
          {[1, 2, 3].map((i) => (
            <div key={i} className="min-w-[280px] bg-zinc-900 rounded-3xl overflow-hidden border border-zinc-800 snap-center shadow-lg">
              <div className="h-40 bg-zinc-800 relative">
                <img 
                  src={`https://images.unsplash.com/photo-1518605368461-1e1e38ce7058?w=500&h=300&fit=crop&q=80&${i}`}
                  alt="News" 
                  className="w-full h-full object-cover opacity-80"
                />
                <div className="absolute top-3 right-3 bg-yellow-500 text-black text-[10px] font-bold px-2 py-1 rounded-md">
                  أخبار الفريق
                </div>
              </div>
              <div className="p-4">
                <h3 className="font-bold text-white text-sm mb-2 line-clamp-2">
                  تحضيرات مكثفة للفريق استعداداً للمباراة القادمة في البطولة
                </h3>
                <div className="flex justify-between items-center text-xs text-zinc-400">
                  <span>منذ ساعتين</span>
                  <button className="text-yellow-500 hover:text-yellow-400 transition-colors font-bold">اقرأ المزيد</button>
                </div>
              </div>
            </div>
          ))}
        </div>"""

news_ui_replace = """        <div className="flex gap-4 overflow-x-auto pb-4 snap-x hide-scrollbar">
          {latestNews.length > 0 ? latestNews.map((news) => (
            <div key={news.id} className="min-w-[280px] bg-zinc-900 rounded-3xl overflow-hidden border border-zinc-800 snap-center shadow-lg">
              <div className="h-40 bg-zinc-800 relative">
                <img 
                  src={news.imageUrl || `https://images.unsplash.com/photo-1518605368461-1e1e38ce7058?w=500&h=300&fit=crop&q=80&${news.id}`}
                  alt={news.title} 
                  className="w-full h-full object-cover opacity-80"
                />
                <div className="absolute top-3 right-3 bg-yellow-500 text-black text-[10px] font-bold px-2 py-1 rounded-md">
                  أخبار الفريق
                </div>
              </div>
              <div className="p-4">
                <h3 className="font-bold text-white text-sm mb-2 line-clamp-2">
                  {news.title}
                </h3>
                <div className="flex justify-between items-center text-xs text-zinc-400">
                  <span>{news.date}</span>
                  <button className="text-yellow-500 hover:text-yellow-400 transition-colors font-bold">اقرأ المزيد</button>
                </div>
              </div>
            </div>
          )) : (
            <p className="text-zinc-500 text-sm px-4">لا توجد أخبار حالياً...</p>
          )}
        </div>"""
content = content.replace(news_ui_search, news_ui_replace)

match_result_search = """        <div className="bg-zinc-900 rounded-3xl p-5 border border-zinc-800 relative overflow-hidden shadow-lg">
          <div className="absolute -top-10 -right-10 w-32 h-32 bg-yellow-500/5 rounded-full blur-2xl"></div>
          <div className="flex justify-between items-center mb-4 relative z-10">
            <span className="text-xs text-zinc-400 bg-zinc-800 px-3 py-1 rounded-full">الرابطة المحترفة الأولى</span>
            <span className="text-xs font-bold text-yellow-500">الجولة 12</span>
          </div>
          
          <div className="flex justify-between items-center relative z-10">
            <div className="flex flex-col items-center gap-2">
              <div className="w-14 h-14 bg-gradient-to-br from-yellow-400 to-yellow-600 rounded-full flex items-center justify-center p-1 shadow-lg">
                <div className="w-full h-full bg-zinc-900 rounded-full flex items-center justify-center font-bold text-xl text-yellow-500">C</div>
              </div>
              <span className="font-bold text-sm text-white">أهلي البرج</span>
            </div>
            
            <div className="flex flex-col items-center">
              <div className="flex items-center gap-3 text-3xl font-black text-white tracking-wider">
                <span>2</span>
                <span className="text-zinc-600">-</span>
                <span className="text-zinc-500">1</span>
              </div>
              <span className="text-[10px] text-zinc-500 mt-1 uppercase tracking-widest">Full Time</span>
            </div>

            <div className="flex flex-col items-center gap-2">
              <div className="w-14 h-14 bg-zinc-800 rounded-full flex items-center justify-center border-2 border-zinc-700 shadow-lg">
                <Shield size={24} className="text-zinc-500" />
              </div>
              <span className="font-bold text-sm text-zinc-400">الفريق الضيف</span>
            </div>
          </div>
        </div>"""
        
match_result_replace = """        <div className="bg-zinc-900 rounded-3xl p-5 border border-zinc-800 relative overflow-hidden shadow-lg">
          <div className="absolute -top-10 -right-10 w-32 h-32 bg-yellow-500/5 rounded-full blur-2xl"></div>
          
          {latestResult ? (
            <>
              <div className="flex justify-between items-center mb-4 relative z-10">
                <span className="text-xs text-zinc-400 bg-zinc-800 px-3 py-1 rounded-full">{latestResult.competition}</span>
                <span className="text-xs font-bold text-yellow-500">{latestResult.date}</span>
              </div>
              
              <div className="flex justify-between items-center relative z-10">
                <div className="flex flex-col items-center gap-2">
                  <div className="w-14 h-14 bg-gradient-to-br from-yellow-400 to-yellow-600 rounded-full flex items-center justify-center p-1 shadow-lg">
                    <div className="w-full h-full bg-zinc-900 rounded-full flex items-center justify-center font-bold text-xl text-yellow-500">{latestResult.homeTeam.charAt(0)}</div>
                  </div>
                  <span className="font-bold text-sm text-white">{latestResult.homeTeam}</span>
                </div>
                
                <div className="flex flex-col items-center">
                  <div className="flex items-center gap-3 text-3xl font-black text-white tracking-wider">
                    <span>{latestResult.homeScore}</span>
                    <span className="text-zinc-600">-</span>
                    <span className="text-zinc-500">{latestResult.awayScore}</span>
                  </div>
                  <span className="text-[10px] text-zinc-500 mt-1 uppercase tracking-widest">Full Time</span>
                </div>

                <div className="flex flex-col items-center gap-2">
                  <div className="w-14 h-14 bg-zinc-800 rounded-full flex items-center justify-center border-2 border-zinc-700 shadow-lg">
                    <span className="font-bold text-xl text-zinc-500">{latestResult.awayTeam.charAt(0)}</span>
                  </div>
                  <span className="font-bold text-sm text-zinc-400">{latestResult.awayTeam}</span>
                </div>
              </div>
            </>
          ) : (
             <p className="text-zinc-500 text-sm text-center">لا توجد نتائج سابقة</p>
          )}
        </div>"""
content = content.replace(match_result_search, match_result_replace)

upcoming_search = """        <div className="bg-gradient-to-br from-zinc-900 to-black rounded-3xl p-5 border border-zinc-800 shadow-lg relative overflow-hidden">
          <div className="absolute inset-0 opacity-10 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-yellow-500 via-transparent to-transparent"></div>
          
          <div className="flex items-center justify-between mb-4 relative z-10">
            <div className="flex items-center gap-2">
              <Calendar size={16} className="text-yellow-500" />
              <span className="text-sm font-bold text-white">السبت 24 أكتوبر</span>
            </div>
            <div className="flex items-center gap-2">
              <Clock size={16} className="text-yellow-500" />
              <span className="text-sm font-bold text-white">18:00</span>
            </div>
          </div>

          <div className="flex justify-between items-center relative z-10 bg-zinc-900/80 p-4 rounded-2xl border border-zinc-800/50 backdrop-blur-sm">
            <div className="text-center w-1/3">
              <h4 className="font-bold text-white text-sm">أهلي البرج</h4>
            </div>
            <div className="w-1/3 flex justify-center">
              <div className="bg-black/50 px-3 py-1.5 rounded-lg border border-yellow-500/20 text-yellow-500 font-bold text-xs tracking-widest">
                VS
              </div>
            </div>
            <div className="text-center w-1/3">
              <h4 className="font-bold text-zinc-400 text-sm">الفريق المنافس</h4>
            </div>
          </div>
          
          <div className="mt-4 flex items-center justify-center gap-2 text-xs text-zinc-500 relative z-10">
            <MapPin size={12} />
            <span>ملعب 20 أوت 1955</span>
          </div>
        </div>"""

upcoming_replace = """        <div className="bg-gradient-to-br from-zinc-900 to-black rounded-3xl p-5 border border-zinc-800 shadow-lg relative overflow-hidden">
          <div className="absolute inset-0 opacity-10 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-yellow-500 via-transparent to-transparent"></div>
          
          {upcomingMatches.length > 0 ? (
            <>
              <div className="flex items-center justify-between mb-4 relative z-10">
                <div className="flex items-center gap-2">
                  <Calendar size={16} className="text-yellow-500" />
                  <span className="text-sm font-bold text-white">{upcomingMatches[0].date}</span>
                </div>
                <div className="flex items-center gap-2">
                  <Clock size={16} className="text-yellow-500" />
                  <span className="text-sm font-bold text-white">{upcomingMatches[0].time}</span>
                </div>
              </div>

              <div className="flex justify-between items-center relative z-10 bg-zinc-900/80 p-4 rounded-2xl border border-zinc-800/50 backdrop-blur-sm">
                <div className="text-center w-1/3">
                  <h4 className="font-bold text-white text-sm">{upcomingMatches[0].homeTeam}</h4>
                </div>
                <div className="w-1/3 flex justify-center">
                  <div className="bg-black/50 px-3 py-1.5 rounded-lg border border-yellow-500/20 text-yellow-500 font-bold text-xs tracking-widest">
                    VS
                  </div>
                </div>
                <div className="text-center w-1/3">
                  <h4 className="font-bold text-zinc-400 text-sm">{upcomingMatches[0].awayTeam}</h4>
                </div>
              </div>
              
              <div className="mt-4 flex items-center justify-center gap-2 text-xs text-zinc-500 relative z-10">
                <MapPin size={12} />
                <span>{upcomingMatches[0].stadium}</span>
              </div>
            </>
          ) : (
            <p className="text-zinc-500 text-sm text-center relative z-10">لا توجد مباريات قادمة مبرمجة</p>
          )}
        </div>"""
content = content.replace(upcoming_search, upcoming_replace)

with open("src/components/Home.tsx", "w") as f:
    f.write(content)

