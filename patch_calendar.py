import sys

with open('src/components/MatchCalendar.tsx', 'r') as f:
    content = f.read()

# Remove showFavoritesOnly and replace with filterStatus
content = content.replace("const [showFavoritesOnly, setShowFavoritesOnly] = useState(false);", "const [filterStatus, setFilterStatus] = useState<'all' | 'past' | 'upcoming'>('all');")
content = content.replace("(!showFavoritesOnly || favorites.includes(m.id))", "(filterStatus === 'all' || m.status === filterStatus)")

# Replace the filter button
old_filter_btn = """          <button 
            onClick={() => setShowFavoritesOnly(!showFavoritesOnly)}
            className={`p-1.5 rounded-full transition-colors ${showFavoritesOnly ? 'bg-yellow-500/20 text-yellow-500' : 'bg-zinc-800 text-zinc-400 hover:text-white'}`}
            title="إظهار المفضلة فقط"
          >
            <Filter size={14} className={showFavoritesOnly ? 'fill-current' : ''} />
          </button>"""

new_filter_btn = """          <div className="flex bg-zinc-800 rounded-lg p-1 text-[10px] font-bold">
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
          </div>"""

if old_filter_btn in content:
    content = content.replace(old_filter_btn, new_filter_btn)
else:
    print("could not find old_filter_btn")


# Ensure addToCalendar uses .ics blob
old_add_to_calendar = """  const addToCalendar = (match: any) => {
    alert(`تمت إضافة مباراة الكابا ضد ${match.opponent} للتقويم`);
  };"""

new_add_to_calendar = """  const addToCalendar = (match: any) => {
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
  };"""

content = content.replace(old_add_to_calendar, new_add_to_calendar)

with open('src/components/MatchCalendar.tsx', 'w') as f:
    f.write(content)
