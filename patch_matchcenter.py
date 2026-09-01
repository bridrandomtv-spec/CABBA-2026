import sys

with open('src/components/MatchCenter.tsx', 'r') as f:
    content = f.read()

# Replace the motm tab content
old_motm = """      {activeTab === 'motm' && (
        <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-5 text-center animate-in fade-in slide-in-from-right-4">
          <Star className="text-yellow-500 w-12 h-12 mx-auto mb-3 drop-shadow-[0_0_15px_rgba(234,179,8,0.5)]" />
          <h3 className="font-bold text-white text-lg mb-2">رجل المباراة</h3>
          <p className="text-xs text-zinc-400 mb-6">صوت للاعب المفضل لديك في هذه المباراة. التصويت يغلق بعد صافرة النهاية.</p>
          
          <div className="space-y-3">
            {['ياسين (10)', 'رياض (9)', 'فوزي (1)'].map((player, i) => (
              <button key={i} className="w-full bg-zinc-800/50 hover:bg-zinc-800 border border-zinc-700 hover:border-yellow-500/50 rounded-xl p-3 flex justify-between items-center transition-colors">
                <span className="font-bold text-sm text-white">{player}</span>
                <div className="w-6 h-6 rounded-full border-2 border-zinc-500 flex items-center justify-center"> 
                  {/* Radio mock */}
                </div>
              </button>
            ))}
          </div>

          <button className="w-full mt-6 bg-yellow-500 hover:bg-yellow-400 text-black text-sm font-bold py-3 rounded-xl transition-colors">
            تأكيد التصويت
          </button>
        </div>
      )}"""

new_motm = """      {activeTab === 'motm' && <MatchMVP />}"""

content = content.replace(old_motm, new_motm)

# Add import
import_statement = "import MatchMVP from './MatchMVP';\n"
content = content.replace("import MatchPredictions from './MatchPredictions';", "import MatchPredictions from './MatchPredictions';\n" + import_statement)


with open('src/components/MatchCenter.tsx', 'w') as f:
    f.write(content)
