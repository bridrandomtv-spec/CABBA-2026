import re

with open("src/components/admin/AdminDashboard.tsx", "r") as f:
    content = f.read()

import_search = "import AdminVideos from './AdminVideos';"
import_replace = "import AdminVideos from './AdminVideos';\nimport AdminStore from './AdminStore';"
content = content.replace(import_search, import_replace)

click_search = "else if (module.id === 'videos') setActiveView('videos');"
click_replace = "else if (module.id === 'videos') setActiveView('videos');\n                else if (module.id === 'store') setActiveView('store');"
content = content.replace(click_search, click_replace)

render_search = "{activeView === 'videos' && <AdminVideos onBack={() => setActiveView('menu')} />}"
render_replace = "{activeView === 'videos' && <AdminVideos onBack={() => setActiveView('menu')} />}\n      {activeView === 'store' && <AdminStore onBack={() => setActiveView('menu')} />}"
content = content.replace(render_search, render_replace)

with open("src/components/admin/AdminDashboard.tsx", "w") as f:
    f.write(content)

