import re

with open("src/components/Profile.tsx", "r") as f:
    content = f.read()

new_auth_logic = """
  const [isLoggedIn, setIsLoggedIn] = useState(() => localStorage.getItem('isLoggedIn') === 'true');
  const [authMode, setAuthMode] = useState<'login' | 'signup'>('login');
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [formErrors, setFormErrors] = useState<string[]>([]);

  const handleAuth = (e: React.FormEvent) => {
    e.preventDefault();
    const errors: string[] = [];
    
    if (authMode === 'signup' && name.trim().length < 3) {
      errors.push("الاسم يجب أن يكون 3 أحرف على الأقل");
    }
    if (!email.includes('@')) {
      errors.push("البريد الإلكتروني غير صالح (يجب أن يحتوي على @)");
    }
    if (password.length < 6) {
      errors.push("كلمة المرور قصيرة جداً (يجب أن تكون 6 أحرف على الأقل)");
    }
    if (authMode === 'signup' && password !== confirmPassword) {
      errors.push("كلمات المرور غير متطابقة");
    }

    if (errors.length > 0) {
      setFormErrors(errors);
      return;
    }

    setFormErrors([]);
    localStorage.setItem('isLoggedIn', 'true');
    // Save mock user data
    if (authMode === 'signup') {
      localStorage.setItem('userName', name);
    }
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
        <div className="text-center space-y-4 mb-8 mt-10">
          <div className="w-24 h-24 mx-auto bg-gradient-to-br from-yellow-400 to-yellow-600 rounded-full flex items-center justify-center border-4 border-zinc-900 shadow-[0_0_30px_rgba(234,179,8,0.3)]">
            <span className="font-bold text-black text-5xl">C</span>
          </div>
          <h2 className="text-2xl font-bold text-white">
            {authMode === 'login' ? 'تسجيل الدخول' : 'إنشاء حساب جديد'}
          </h2>
          <p className="text-sm text-zinc-400">
            {authMode === 'login' 
              ? 'سجل دخولك للانضمام إلى مجتمع أنصار الجراد الأصفر.'
              : 'أنشئ حسابك الآن لتصبح جزءاً من العائلة الصفراء.'}
          </p>
        </div>

        <form onSubmit={handleAuth} className="space-y-4 max-w-sm mx-auto w-full pb-10">
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

          {authMode === 'signup' && (
            <div className="space-y-2">
              <label className="text-sm font-bold text-zinc-400">الاسم الكامل</label>
              <input 
                value={name}
                onChange={(e) => setName(e.target.value)}
                required={authMode === 'signup'} 
                type="text" 
                placeholder="أمين ب." 
                className="w-full bg-zinc-900 border border-zinc-800 rounded-xl p-4 text-white text-right focus:outline-none focus:border-yellow-500 transition-colors" 
              />
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

          {authMode === 'signup' && (
            <div className="space-y-2">
              <label className="text-sm font-bold text-zinc-400">تأكيد كلمة المرور</label>
              <input 
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                required={authMode === 'signup'} 
                type="password" 
                placeholder="••••••••" 
                className="w-full bg-zinc-900 border border-zinc-800 rounded-xl p-4 text-white text-right focus:outline-none focus:border-yellow-500 transition-colors" 
              />
            </div>
          )}
          
          <div className="flex justify-between items-center px-1">
            {authMode === 'login' ? (
              <>
                <button type="button" onClick={() => alert('سيتم إرسال رابط إعادة تعيين كلمة المرور.')} className="text-xs text-yellow-500 font-bold hover:underline">
                  هل نسيت كلمة المرور؟
                </button>
                <button type="button" onClick={() => { setAuthMode('signup'); setFormErrors([]); }} className="text-xs text-zinc-400 font-bold hover:text-white transition-colors">
                  إنشاء حساب جديد
                </button>
              </>
            ) : (
              <button type="button" onClick={() => { setAuthMode('login'); setFormErrors([]); }} className="text-xs text-zinc-400 font-bold hover:text-white transition-colors w-full text-center">
                لديك حساب بالفعل؟ تسجيل الدخول
              </button>
            )}
          </div>

          <button type="submit" className="w-full bg-yellow-500 hover:bg-yellow-400 text-black font-bold text-lg p-4 rounded-xl shadow-[0_0_15px_rgba(234,179,8,0.4)] transition-all mt-4">
            {authMode === 'login' ? 'تسجيل الدخول' : 'إنشاء حساب'}
          </button>
        </form>
      </div>
    );
  }
"""

start_pattern = r"  const \[isLoggedIn, setIsLoggedIn\] = useState\(\(\) => localStorage\.getItem\('isLoggedIn'\) === 'true'\);"
end_pattern = r"    \);\n  }"

content = re.sub(start_pattern + r".*?" + end_pattern, new_auth_logic, content, flags=re.DOTALL)

with open("src/components/Profile.tsx", "w") as f:
    f.write(content)

