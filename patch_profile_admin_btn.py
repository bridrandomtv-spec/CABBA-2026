import re

with open("src/components/Profile.tsx", "r") as f:
    content = f.read()

btn_search = """      <div className="space-y-3 mb-6">
        <h4 className="text-zinc-400 font-bold text-xs mb-2">إعدادات</h4>"""
        
btn_replace = """      <div className="space-y-3 mb-6">
        <h4 className="text-zinc-400 font-bold text-xs mb-2">إعدادات</h4>
        {userData?.role === 'admin' && (
          <button 
            onClick={() => window.dispatchEvent(new CustomEvent('navigate', { detail: 'admin' }))}
            className="w-full bg-yellow-500/10 hover:bg-yellow-500/20 border border-yellow-500/50 p-4 rounded-xl flex items-center justify-between transition-colors group mb-3"
          >
            <span className="text-sm text-yellow-500 font-bold group-hover:text-yellow-400 transition-colors">لوحة الإدارة (Admin Panel)</span>
            <Shield size={16} className="text-yellow-500 group-hover:text-yellow-400 transition-colors" />
          </button>
        )}"""
content = content.replace(btn_search, btn_replace)

with open("src/components/Profile.tsx", "w") as f:
    f.write(content)

