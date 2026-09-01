import sys

with open('src/components/Profile.tsx', 'r') as f:
    content = f.read()

old_btn = """        <button 
          onClick={toggleTheme}
          className="w-full bg-zinc-900 hover:bg-zinc-800 border border-zinc-800/50 p-4 rounded-xl flex items-center justify-between transition-colors"
        >
          <div className="flex items-center gap-3">
            {theme === 'dark' ? <Moon size={18} className="text-zinc-400" /> : <Sun size={18} className="text-zinc-400" />}
            <span className="text-sm text-white font-medium">
              {theme === 'dark' ? 'الوضع الليلي' : 'الوضع النهاري'}
            </span>
          </div>
          <div className={`w-12 h-6 rounded-full transition-colors relative flex items-center ${theme === 'dark' ? 'bg-zinc-700' : 'bg-yellow-500'}`}>
            <div className={`w-4 h-4 rounded-full bg-white absolute top-1 transition-transform ${theme === 'dark' ? 'right-1' : 'left-1'}`}></div>
          </div>
        </button>"""

new_btn = """        <button 
          onClick={toggleTheme}
          className="w-full bg-zinc-900 hover:bg-zinc-800 border border-zinc-800/50 p-4 rounded-xl flex items-center justify-between transition-colors"
        >
          <div className="flex items-center gap-3">
            {theme === 'dark' ? <Moon size={18} className="text-yellow-500" /> : <Sun size={18} className="text-yellow-500" />}
            <span className="text-sm text-white font-medium">
              المظهر (الليلي / النهاري)
            </span>
          </div>
          <div className={`w-12 h-6 rounded-full transition-colors relative flex items-center ${theme === 'dark' ? 'bg-zinc-700' : 'bg-yellow-500'}`}>
            <div className={`w-4 h-4 rounded-full bg-white absolute top-1 transition-transform ${theme === 'dark' ? 'right-1' : 'left-1'}`}></div>
          </div>
        </button>"""

content = content.replace(old_btn, new_btn)

with open('src/components/Profile.tsx', 'w') as f:
    f.write(content)
