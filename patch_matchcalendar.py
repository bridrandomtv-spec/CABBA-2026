import sys
with open('src/components/MatchCalendar.tsx', 'r') as f:
    content = f.read()

# Imports
import_statement = "import { Calendar, MapPin, Bell, CalendarPlus, ChevronRight, ChevronLeft, Heart, Filter } from 'lucide-react';\nimport { useFavorites } from '../hooks/useFavorites';"
content = content.replace("import { Calendar, MapPin, Bell, CalendarPlus, ChevronRight, ChevronLeft } from 'lucide-react';", import_statement)

# State and hooks
state_statement = """  const [currentMonthIndex, setCurrentMonthIndex] = useState(2); // Default to March (index 2 for Jan, Feb, Mar)
  const [showFavoritesOnly, setShowFavoritesOnly] = useState(false);
  const { favorites, toggleFavorite } = useFavorites();
"""
content = content.replace("  const [currentMonthIndex, setCurrentMonthIndex] = useState(2); // Default to March (index 2 for Jan, Feb, Mar)", state_statement)

# Export matches data
matches_data = """  const matches = [
    { id: 1, date: '15 فيفري', day: 15, time: '14:30', opponent: 'مولودية وهران', type: 'الرابطة المحترفة الأولى', location: 'ملعب 20 أوت', status: 'past', score: '2 - 0', month: 1 },
    { id: 2, date: '25 فيفري', day: 25, time: '16:00', opponent: 'شباب بلوزداد', type: 'الرابطة المحترفة الأولى', location: 'ملعب 20 أوت 1955', status: 'past', score: '1 - 1', month: 1 },
    { id: 3, date: '05 مارس', day: 5, time: '15:00', opponent: 'شبيبة القبائل', type: 'الرابطة المحترفة الأولى', location: 'ملعب 1 نوفمبر', status: 'past', score: '1 - 2', month: 2 },
    { id: 4, date: '15 مارس', day: 15, time: '14:30', opponent: 'مولودية الجزائر', type: 'الرابطة المحترفة الأولى', location: 'ملعب 5 جويلية', status: 'upcoming', month: 2 },
    { id: 5, date: '22 مارس', day: 22, time: '16:00', opponent: 'وفاق سطيف', type: 'الرابطة المحترفة الأولى', location: 'ملعب 20 أوت', status: 'upcoming', month: 2 },
    { id: 6, date: '04 أفريل', day: 4, time: '15:00', opponent: 'اتحاد العاصمة', type: 'الرابطة المحترفة الأولى', location: 'ملعب عمر حمادي', status: 'upcoming', month: 3 },
    { id: 7, date: '18 أفريل', day: 18, time: '16:00', opponent: 'نجم مقرة', type: 'الرابطة المحترفة الأولى', location: 'ملعب 20 أوت', status: 'upcoming', month: 3 },
  ];
"""
export_matches = """export const MATCHES_DATA = [
  { id: 1, date: '15 فيفري', day: 15, time: '14:30', opponent: 'مولودية وهران', type: 'الرابطة المحترفة الأولى', location: 'ملعب 20 أوت', status: 'past', score: '2 - 0', month: 1 },
  { id: 2, date: '25 فيفري', day: 25, time: '16:00', opponent: 'شباب بلوزداد', type: 'الرابطة المحترفة الأولى', location: 'ملعب 20 أوت 1955', status: 'past', score: '1 - 1', month: 1 },
  { id: 3, date: '05 مارس', day: 5, time: '15:00', opponent: 'شبيبة القبائل', type: 'الرابطة المحترفة الأولى', location: 'ملعب 1 نوفمبر', status: 'past', score: '1 - 2', month: 2 },
  { id: 4, date: '15 مارس', day: 15, time: '14:30', opponent: 'مولودية الجزائر', type: 'الرابطة المحترفة الأولى', location: 'ملعب 5 جويلية', status: 'upcoming', month: 2 },
  { id: 5, date: '22 مارس', day: 22, time: '16:00', opponent: 'وفاق سطيف', type: 'الرابطة المحترفة الأولى', location: 'ملعب 20 أوت', status: 'upcoming', month: 2 },
  { id: 6, date: '04 أفريل', day: 4, time: '15:00', opponent: 'اتحاد العاصمة', type: 'الرابطة المحترفة الأولى', location: 'ملعب عمر حمادي', status: 'upcoming', month: 3 },
  { id: 7, date: '18 أفريل', day: 18, time: '16:00', opponent: 'نجم مقرة', type: 'الرابطة المحترفة الأولى', location: 'ملعب 20 أوت', status: 'upcoming', month: 3 },
];\n"""
if "export const MATCHES_DATA" not in content:
    content = content.replace("export default function MatchCalendar() {", export_matches + "\nexport default function MatchCalendar() {")

content = content.replace(matches_data, "  const matches = MATCHES_DATA;\n")

# Filters
filter_statement = """  const filteredMatches = matches.filter(m => m.month === currentMonthIndex && (!showFavoritesOnly || favorites.includes(m.id)));"""
content = content.replace("  const filteredMatches = matches.filter(m => m.month === currentMonthIndex);", filter_statement)


header = """      <div className="flex items-center justify-between mb-4">
        <h3 className="font-bold text-white text-lg flex items-center gap-2">
          <Calendar className="text-yellow-500" size={20} />
          التقويم
        </h3>
        
        <div className="flex items-center gap-3 bg-zinc-900 border border-zinc-800 rounded-full px-3 py-1">"""
new_header = """      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <h3 className="font-bold text-white text-lg flex items-center gap-2">
            <Calendar className="text-yellow-500" size={20} />
            التقويم
          </h3>
          <button 
            onClick={() => setShowFavoritesOnly(!showFavoritesOnly)}
            className={`p-1.5 rounded-full transition-colors ${showFavoritesOnly ? 'bg-yellow-500/20 text-yellow-500' : 'bg-zinc-800 text-zinc-400 hover:text-white'}`}
            title="إظهار المفضلة فقط"
          >
            <Filter size={14} className={showFavoritesOnly ? 'fill-current' : ''} />
          </button>
        </div>
        
        <div className="flex items-center gap-3 bg-zinc-900 border border-zinc-800 rounded-full px-3 py-1">"""
content = content.replace(header, new_header)

# Heart icon
old_card_header = """                <div className="flex justify-between items-center pb-3 border-b border-zinc-800/50">
                  <span className="text-[10px] font-bold text-zinc-500 bg-zinc-800 px-2 py-1 rounded">{match.type}</span>
                  <div className="flex items-center gap-1.5 text-xs font-bold text-zinc-400">
                    <Calendar size={12} />
                    <span>{match.date}</span>
                  </div>
                </div>"""
new_card_header = """                <div className="flex justify-between items-center pb-3 border-b border-zinc-800/50">
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
                </div>"""
content = content.replace(old_card_header, new_card_header)

with open('src/components/MatchCalendar.tsx', 'w') as f:
    f.write(content)
