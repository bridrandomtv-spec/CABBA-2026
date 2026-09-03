import re

with open("src/components/Profile.tsx", "r") as f:
    content = f.read()

# Add useState to imports
if "import { useState" not in content:
    content = content.replace("import { Award,", "import { useState } from 'react';\nimport { Award,")

# Add state and login UI
profile_start = "export default function Profile() {"
state_addition = """
  const [isLoggedIn, setIsLoggedIn] = useState(() => localStorage.getItem('isLoggedIn') === 'true');

  const handleLogin = (e: React.FormEvent) => {
    e.preventDefault();
    localStorage.setItem('isLoggedIn', 'true');
    setIsLoggedIn(true);
  };

  const handleLogout = () => {
    localStorage.removeItem('isLoggedIn');
    setIsLoggedIn(false);
    alert("تم تسجيل الخروج بنجاح");
  };

  if (!isLoggedIn) {
    return (
      <div className="p-4 space-y-6 h-full flex flex-col justify-center animate-in fade-in slide-in-from-bottom-4 duration-500" dir="rtl">
        <div className="text-center space-y-4 mb-8">
          <div className="w-24 h-24 mx-auto bg-gradient-to-br from-yellow-400 to-yellow-600 rounded-full flex items-center justify-center border-4 border-zinc-900 shadow-[0_0_30px_rgba(234,179,8,0.3)]">
            <span className="font-bold text-black text-5xl">C</span>
          </div>
          <h2 className="text-2xl font-bold text-white">تسجيل الدخول</h2>
          <p className="text-sm text-zinc-400">سجل دخولك للانضمام إلى مجتمع أنصار الجراد الأصفر وتخصيص تجربتك.</p>
        </div>

        <form onSubmit={handleLogin} className="space-y-4 max-w-sm mx-auto w-full">
          <div className="space-y-2">
            <label className="text-sm font-bold text-zinc-400">البريد الإلكتروني</label>
            <input required type="email" placeholder="supporter@cabba.dz" className="w-full bg-zinc-900 border border-zinc-800 rounded-xl p-4 text-white text-right focus:outline-none focus:border-yellow-500 transition-colors" />
          </div>
          <div className="space-y-2">
            <label className="text-sm font-bold text-zinc-400">كلمة المرور</label>
            <input required type="password" placeholder="••••••••" className="w-full bg-zinc-900 border border-zinc-800 rounded-xl p-4 text-white text-right focus:outline-none focus:border-yellow-500 transition-colors" />
          </div>
          <button type="submit" className="w-full bg-yellow-500 hover:bg-yellow-400 text-black font-bold text-lg p-4 rounded-xl shadow-[0_0_15px_rgba(234,179,8,0.4)] transition-all">
            تسجيل الدخول
          </button>
        </form>
      </div>
    );
  }
"""

content = content.replace(profile_start, profile_start + state_addition)

# Replace the logout button onClick
old_logout = """onClick={() => {
          alert("تم تسجيل الخروج بنجاح");
          window.location.reload();
        }}"""

content = content.replace(old_logout, "onClick={handleLogout}")

with open("src/components/Profile.tsx", "w") as f:
    f.write(content)

