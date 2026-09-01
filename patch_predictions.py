import sys

with open('src/components/MatchPredictions.tsx', 'r') as f:
    content = f.read()

# Make sure BarChart is imported if we add a chart
if 'BarChart' not in content:
    content = content.replace("import { useState } from 'react';", "import { useState } from 'react';\nimport { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell } from 'recharts';")

old_leaderboard = """  const leaderboard = [
    { rank: 1, name: 'سفيان البرجي', points: 1250, badge: '🔥' },
    { rank: 2, name: 'عاشق الكابا', points: 1120, badge: '⭐' },
    { rank: 3, name: 'أمين CABBA', points: 980, badge: '⚡' },
    { rank: 4, name: 'أحمد 34', points: 850, badge: '' },
    { rank: 5, name: 'محمد الأمين', points: 790, badge: '' },
  ];"""

new_leaderboard = """  const leaderboard = [
    { rank: 1, name: 'سفيان البرجي', points: 1250, accuracy: 82, badge: '🔥' },
    { rank: 2, name: 'عاشق الكابا', points: 1120, accuracy: 75, badge: '⭐' },
    { rank: 3, name: 'أمين CABBA', points: 980, accuracy: 68, badge: '⚡' },
    { rank: 4, name: 'أحمد 34', points: 850, accuracy: 62, badge: '' },
    { rank: 5, name: 'محمد الأمين', points: 790, accuracy: 58, badge: '' },
    { rank: 142, name: 'أنت', points: 320, accuracy: 45, badge: '' },
  ];
  
  const accuracyData = [
    { name: 'المتصدر', accuracy: 82, fill: '#eab308' },
    { name: 'المتوسط', accuracy: 55, fill: '#71717a' },
    { name: 'أنت', accuracy: 45, fill: '#ef4444' },
  ];"""

content = content.replace(old_leaderboard, new_leaderboard)

old_leaderboard_card = """      {/* Leaderboard Card */}
      <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-5 shadow-lg relative overflow-hidden">
        <div className="flex items-center justify-between mb-5">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-yellow-500/10 rounded-full flex items-center justify-center text-yellow-500">
                <Trophy size={20} />
              </div>
              <h3 className="font-bold text-white text-md">لوحة الصدارة</h3>
            </div>
            <button className="text-xs text-zinc-400 flex items-center gap-1 hover:text-white transition-colors">
                هذا الأسبوع <ChevronDown size={14} />
            </button>
        </div>
        <div className="space-y-3">
            {leaderboard.map((user, index) => (
                <div key={user.rank} className={`flex items-center justify-between p-3 rounded-xl border ${index === 0 ? 'bg-yellow-500/5 border-yellow-500/20' : 'bg-zinc-800/30 border-zinc-700/30'}`}>
                    <div className="flex items-center gap-3">
                        <div className={`w-8 h-8 rounded-full flex items-center justify-center font-bold text-xs ${
                            index === 0 ? 'bg-yellow-500 text-black shadow-[0_0_10px_rgba(234,179,8,0.3)]' : 
                            index === 1 ? 'bg-zinc-300 text-zinc-900' : 
                            index === 2 ? 'bg-amber-700 text-white' : 
                            'bg-zinc-800 text-zinc-400 border border-zinc-700'
                        }`}>
                            {user.rank}
                        </div>
                        <div>
                            <div className="flex items-center gap-1">
                                <span className={`font-bold text-sm ${index === 0 ? 'text-yellow-500' : 'text-white'}`}>{user.name}</span>
                                {user.badge && <span className="text-xs">{user.badge}</span>}
                            </div>
                        </div>
                    </div>
                    <div className="flex items-center gap-1.5">
                        <span className="font-black text-white text-sm">{user.points}</span>
                        <span className="text-[10px] text-zinc-500 font-bold">نقطة</span>
                    </div>
                </div>
            ))}
        </div>
      </div>"""

new_leaderboard_card = """      {/* Accuracy Comparison Chart */}
      <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-5 shadow-lg">
        <div className="flex items-center gap-3 mb-4">
          <div className="w-10 h-10 bg-blue-500/10 rounded-full flex items-center justify-center text-blue-500">
            <Activity size={20} />
          </div>
          <div>
            <h3 className="font-bold text-white text-md">دقة التوقعات</h3>
            <p className="text-[10px] text-zinc-400">مقارنة نسبة نجاح توقعاتك مع البقية</p>
          </div>
        </div>
        <div className="h-[120px] w-full" dir="ltr">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={accuracyData} layout="vertical" margin={{ top: 0, right: 0, left: 0, bottom: 0 }}>
              <XAxis type="number" hide domain={[0, 100]} />
              <YAxis dataKey="name" type="category" width={60} stroke="#a1a1aa" fontSize={10} tickLine={false} axisLine={false} />
              <Tooltip 
                cursor={{ fill: '#27272a' }}
                contentStyle={{ backgroundColor: '#18181b', borderColor: '#27272a', borderRadius: '8px', textAlign: 'right' }}
                itemStyle={{ color: '#fff', fontSize: '12px', fontWeight: 'bold' }}
                formatter={(value) => [`${value}%`, 'الدقة']}
              />
              <Bar dataKey="accuracy" radius={[0, 4, 4, 0]} barSize={16}>
                {accuracyData.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={entry.fill} />
                ))}
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Leaderboard Card */}
      <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-5 shadow-lg relative overflow-hidden">
        <div className="flex items-center justify-between mb-5">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-yellow-500/10 rounded-full flex items-center justify-center text-yellow-500">
                <Trophy size={20} />
              </div>
              <h3 className="font-bold text-white text-md">التصنيف العالمي</h3>
            </div>
            <button className="text-xs text-zinc-400 flex items-center gap-1 hover:text-white transition-colors">
                العالمي <ChevronDown size={14} />
            </button>
        </div>
        <div className="space-y-3">
            {leaderboard.map((user, index) => {
                const isCurrentUser = user.name === 'أنت';
                return (
                <div key={user.rank} className={`flex items-center justify-between p-3 rounded-xl border ${index === 0 ? 'bg-yellow-500/5 border-yellow-500/20' : isCurrentUser ? 'bg-zinc-800 border-zinc-600' : 'bg-zinc-800/30 border-zinc-700/30'}`}>
                    <div className="flex items-center gap-3">
                        <div className={`w-8 h-8 rounded-full flex items-center justify-center font-bold text-xs ${
                            index === 0 ? 'bg-yellow-500 text-black shadow-[0_0_10px_rgba(234,179,8,0.3)]' : 
                            index === 1 ? 'bg-zinc-300 text-zinc-900' : 
                            index === 2 ? 'bg-amber-700 text-white' : 
                            'bg-zinc-800 text-zinc-400 border border-zinc-700'
                        }`}>
                            {user.rank}
                        </div>
                        <div>
                            <div className="flex items-center gap-1">
                                <span className={`font-bold text-sm ${index === 0 ? 'text-yellow-500' : isCurrentUser ? 'text-white' : 'text-zinc-200'}`}>{user.name}</span>
                                {user.badge && <span className="text-xs">{user.badge}</span>}
                            </div>
                            <div className="text-[10px] text-zinc-500">
                              الدقة: <span className={user.accuracy >= 70 ? 'text-green-500' : user.accuracy >= 50 ? 'text-yellow-500' : 'text-zinc-400'}>{user.accuracy}%</span>
                            </div>
                        </div>
                    </div>
                    <div className="flex items-center gap-1.5">
                        <span className="font-black text-white text-sm">{user.points}</span>
                        <span className="text-[10px] text-zinc-500 font-bold">نقطة</span>
                    </div>
                </div>
            )})}
        </div>
      </div>"""

content = content.replace(old_leaderboard_card, new_leaderboard_card)

with open('src/components/MatchPredictions.tsx', 'w') as f:
    f.write(content)
