import re

with open("src/components/Profile.tsx", "r") as f:
    content = f.read()

# Make sure AlertCircle is imported
if "AlertCircle" not in content:
    content = content.replace("import { Award,", "import { Award, AlertCircle,")

new_login_logic = """
  const [isLoggedIn, setIsLoggedIn] = useState(() => localStorage.getItem('isLoggedIn') === 'true');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [formErrors, setFormErrors] = useState<string[]>([]);

  const handleLogin = (e: React.FormEvent) => {
    e.preventDefault();
    const errors: string[] = [];
    
    if (!email.includes('@')) {
      errors.push("البريد الإلكتروني غير صالح (يجب أن يحتوي على @)");
    }
    if (password.length < 6) {
      errors.push("كلمة المرور قصيرة جداً (يجب أن تكون 6 أحرف على الأقل)");
    }

    if (errors.length > 0) {
      setFormErrors(errors);
      return;
    }

    setFormErrors([]);
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
          {formErrors.length > 0 && (
            <div className="bg-red-500/10 border border-red-500/20 rounded-xl p-4 mb-4 text-right">
              <div className="flex items-center gap-2 text-red-500 font-bold text-sm mb-2">
                <AlertCircle size={16} />
                <span>Fix errors ({formErrors.length} أخطاء):</span>
              </div>
              <ul className="list-disc list-inside text-xs text-red-400 space-y-1">
                {formErrors.map((err, i) => <li key={i}>{err}</li>)}
              </ul>
            </div>
          )}

          <div className="space-y-2">
            <label className="text-sm font-bold text-zinc-400">البريد الإلكتروني</label>
            <input 
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required 
              type="email" 
              placeholder="supporter@cabba.dz" 
              className="w-full bg-zinc-900 border border-zinc-800 rounded-xl p-4 text-white text-right focus:outline-none focus:border-yellow-500 transition-colors" 
            />
          </div>
          <div className="space-y-2">
            <label className="text-sm font-bold text-zinc-400">كلمة المرور</label>
            <input 
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required 
              type="password" 
              placeholder="••••••••" 
              className="w-full bg-zinc-900 border border-zinc-800 rounded-xl p-4 text-white text-right focus:outline-none focus:border-yellow-500 transition-colors" 
            />
          </div>
          
          <div className="flex justify-between items-center px-1">
            <button type="button" onClick={() => alert('سيتم إرسال رابط إعادة تعيين كلمة المرور.')} className="text-xs text-yellow-500 font-bold hover:underline">
              هل نسيت كلمة المرور؟
            </button>
            <button type="button" onClick={() => alert('قريباً: إنشاء حساب جديد.')} className="text-xs text-zinc-400 font-bold hover:text-white transition-colors">
              إنشاء حساب جديد
            </button>
          </div>

          <button type="submit" className="w-full bg-yellow-500 hover:bg-yellow-400 text-black font-bold text-lg p-4 rounded-xl shadow-[0_0_15px_rgba(234,179,8,0.4)] transition-all mt-4">
            تسجيل الدخول
          </button>
        </form>
      </div>
    );
  }
"""

start_pattern = r"  const \[isLoggedIn, setIsLoggedIn\] = useState\(\(\) => localStorage\.getItem\('isLoggedIn'\) === 'true'\);"
end_pattern = r"    \);\n  }"

content = re.sub(start_pattern + r".*?" + end_pattern, new_login_logic, content, flags=re.DOTALL)

with open("src/components/Profile.tsx", "w") as f:
    f.write(content)

