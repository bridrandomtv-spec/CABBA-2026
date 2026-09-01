import sys

with open('src/components/MatchCenter.tsx', 'r') as f:
    content = f.read()

# Add import
if 'import PlayerComparison from' not in content:
    content = content.replace("import SeasonStats from './SeasonStats';", "import SeasonStats from './SeasonStats';\nimport PlayerComparison from './PlayerComparison';\nimport { GitCompare } from 'lucide-react';")

# State
old_state = "useState<'live' | 'stats' | 'season' | 'formation' | 'motm' | 'travel' | 'predictions' | 'calendar' | 'tickets' | 'scout'>('live');"
new_state = "useState<'live' | 'stats' | 'season' | 'compare' | 'formation' | 'motm' | 'travel' | 'predictions' | 'calendar' | 'tickets' | 'scout'>('live');"
content = content.replace(old_state, new_state)

# Tab button
old_compare_btn = """        <button 
          onClick={() => setActiveTab('scout')}
          className={`flex-none px-4 flex justify-center items-center gap-2 py-2 text-xs font-bold rounded-lg transition-colors ${activeTab === 'scout' ? 'bg-zinc-800 text-yellow-500 shadow-sm' : 'text-zinc-500'}`}
        >
          <Target size={14} /> كشاف المباراة
        </button>"""
        
new_compare_btn = """        <button 
          onClick={() => setActiveTab('compare')}
          className={`flex-none px-4 flex justify-center items-center gap-2 py-2 text-xs font-bold rounded-lg transition-colors ${activeTab === 'compare' ? 'bg-zinc-800 text-yellow-500 shadow-sm' : 'text-zinc-500'}`}
        >
          <GitCompare size={14} /> مقارنة اللاعبين
        </button>\n""" + old_compare_btn

if "<GitCompare size={14} /> مقارنة اللاعبين" not in content:
    content = content.replace(old_compare_btn, new_compare_btn)

# Tab content
old_stats_content = """      {activeTab === 'season' && <SeasonStats />}"""
new_stats_content = old_stats_content + """
      {activeTab === 'compare' && <PlayerComparison />}"""

if "{activeTab === 'compare' && <PlayerComparison />}" not in content:
    content = content.replace(old_stats_content, new_stats_content)

with open('src/components/MatchCenter.tsx', 'w') as f:
    f.write(content)
