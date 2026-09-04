import re

with open("src/components/admin/AdminDashboard.tsx", "r") as f:
    content = f.read()

import_search = "import {\n  Users, Newspaper, Trophy, MessageSquare, Music,\n  Video, ShoppingBag, ShieldAlert, Settings, ChevronRight\n} from 'lucide-react';"
import_replace = "import { useState } from 'react';\nimport {\n  Users, Newspaper, Trophy, MessageSquare, Music,\n  Video, ShoppingBag, ShieldAlert, Settings, ChevronRight\n} from 'lucide-react';\nimport AdminNews from './AdminNews';"
content = content.replace("import { useState } from 'react';\nimport { \n  Users, Newspaper, Trophy, MessageSquare, Music, \n  Video, ShoppingBag, ShieldAlert, Settings, ChevronRight\n} from 'lucide-react';", import_replace)

view_search = "  const [activeView, setActiveView] = useState<'menu' | 'news'>('menu');"
view_replace = "  const [activeView, setActiveView] = useState<'menu' | 'news' | 'matches' | 'users' | 'chants' | 'videos' | 'store'>('menu');"
content = content.replace(view_search, view_replace)

news_render_search = """      {activeView === 'news' && (
        <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-4">
          <button 
            onClick={() => setActiveView('menu')}
            className="flex items-center gap-2 text-yellow-500 text-sm font-bold mb-4"
          >
            <ChevronRight size={16} />
            العودة للقائمة
          </button>
          <div className="text-center py-10">
            <Newspaper size={48} className="mx-auto text-zinc-600 mb-3" />
            <p className="text-white font-bold">وحدة إدارة الأخبار</p>
            <p className="text-sm text-zinc-500">سيتم ربطها بقاعدة البيانات في المرحلة القادمة</p>
          </div>
        </div>
      )}"""

news_render_replace = """      {activeView === 'news' && <AdminNews onBack={() => setActiveView('menu')} />}"""
content = content.replace(news_render_search, news_render_replace)

with open("src/components/admin/AdminDashboard.tsx", "w") as f:
    f.write(content)

