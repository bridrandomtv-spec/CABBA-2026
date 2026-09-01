import sys

with open('src/components/MatchCenter.tsx', 'r') as f:
    content = f.read()

# 1. Add import
if 'MatchArchive' not in content:
    content = content.replace("import MatchAbsences from './MatchAbsences';", "import MatchAbsences from './MatchAbsences';\nimport MatchArchive from './MatchArchive';")

# 2. Add Tab Button (e.g. before Scout or at the end of tabs)
old_scout_tab = """        <button 
          onClick={() => setActiveTab('scout')}
          className={`flex-none px-4 flex justify-center items-center gap-2 py-2 text-xs font-bold rounded-lg transition-colors ${activeTab === 'scout' ? 'bg-zinc-800 text-yellow-500 shadow-sm' : 'text-zinc-500'}`}
        >
          <Target size={14} /> كشاف المباراة
        </button>"""

new_scout_archive_tab = """        <button 
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
        </button>"""

if old_scout_tab in content:
    content = content.replace(old_scout_tab, new_scout_archive_tab)
else:
    print("Could not find scout tab")

# Add History icon import
if 'History' not in content:
    content = content.replace("import { Activity, BarChart3, Users, Star, TrendingUp, Calendar, Trophy, Zap, AlertCircle, Share2, MapPin, Search, ChevronRight, Bus, CheckCircle, Ticket, GitCompare, Target, PieChartIcon } from 'lucide-react';", "import { Activity, BarChart3, Users, Star, TrendingUp, Calendar, Trophy, Zap, AlertCircle, Share2, MapPin, Search, ChevronRight, Bus, CheckCircle, Ticket, GitCompare, Target, PieChartIcon, History } from 'lucide-react';")
    content = content.replace("import { Activity, BarChart3, Users, Star, TrendingUp, Calendar, Trophy, Zap, MapPin, Bus, CheckCircle, Ticket, GitCompare, Target, PieChartIcon } from 'lucide-react';", "import { Activity, BarChart3, Users, Star, TrendingUp, Calendar, Trophy, Zap, MapPin, Bus, CheckCircle, Ticket, GitCompare, Target, PieChartIcon, History } from 'lucide-react';")

# 3. Add Content View
old_scout_content = """      {activeTab === 'scout' && <MatchScout />}
    </div>
  );
}"""

new_scout_archive_content = """      {activeTab === 'scout' && <MatchScout />}
      {activeTab === 'archive' && <MatchArchive />}
    </div>
  );
}"""

if old_scout_content in content:
    content = content.replace(old_scout_content, new_scout_archive_content)
else:
    print("Could not find scout content")

with open('src/components/MatchCenter.tsx', 'w') as f:
    f.write(content)
