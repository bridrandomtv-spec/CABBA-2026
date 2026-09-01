import sys

with open('src/components/Profile.tsx', 'r') as f:
    content = f.read()

import_statement = "import { Award, Shield, Settings, CheckCircle2, ChevronLeft, Moon, Sun, Heart, Calendar as CalendarIcon, MapPin } from 'lucide-react';\nimport { useFavorites } from '../hooks/useFavorites';\nimport { MATCHES_DATA } from './MatchCalendar';"
content = content.replace("import { Award, Shield, Settings, CheckCircle2, ChevronLeft, Moon, Sun } from 'lucide-react';", import_statement)

use_fav_hook = """  const { theme, toggleTheme } = useTheme();
  const { favorites } = useFavorites();
  const favoriteMatches = MATCHES_DATA.filter(m => favorites.includes(m.id));"""
content = content.replace("  const { theme, toggleTheme } = useTheme();", use_fav_hook)

fav_section = """      {/* Favorite Matches */}
      <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-5 shadow-sm">
        <div className="flex items-center justify-between mb-4">
          <h3 className="font-bold text-white text-lg flex items-center gap-2">
            <Heart className="text-red-500 fill-current" size={20} />
            المباريات المفضلة
          </h3>
          <span className="text-xs text-zinc-500 font-bold bg-zinc-800 px-2 py-1 rounded-md">{favorites.length} مباريات</span>
        </div>
        
        <div className="space-y-3">
          {favoriteMatches.length > 0 ? (
            favoriteMatches.map(match => (
              <div key={match.id} className="bg-zinc-800/50 border border-zinc-700/50 rounded-xl p-3 flex justify-between items-center">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 bg-zinc-800 rounded-full flex items-center justify-center border-2 border-zinc-700">
                    <span className="font-bold text-xs text-white truncate max-w-[20px]">{match.opponent.charAt(0)}</span>
                  </div>
                  <div>
                    <h4 className="font-bold text-white text-sm">{match.opponent}</h4>
                    <div className="flex items-center gap-1 text-[10px] text-zinc-500 mt-0.5">
                      <CalendarIcon size={10} /> {match.date}
                    </div>
                  </div>
                </div>
                <div className="flex flex-col items-center">
                  {match.status === 'past' ? (
                    <span className="font-bold text-white tracking-widest">{match.score}</span>
                  ) : (
                    <span className="text-xs font-bold text-yellow-500">{match.time}</span>
                  )}
                </div>
              </div>
            ))
          ) : (
            <div className="text-center py-6">
              <Heart size={32} className="text-zinc-700 mx-auto mb-2" />
              <p className="text-xs text-zinc-500">لم تقم بإضافة أي مباراة للمفضلة بعد.</p>
            </div>
          )}
        </div>
      </div>

      {/* Gamification / Loyalty Points */}"""

content = content.replace("      {/* Gamification / Loyalty Points */}", fav_section)

with open('src/components/Profile.tsx', 'w') as f:
    f.write(content)
