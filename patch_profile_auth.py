import re

with open("src/components/Profile.tsx", "r") as f:
    content = f.read()

# Make sure signInWithEmailAndPassword, createUserWithEmailAndPassword are imported
if "signInWithEmailAndPassword" not in content:
    content = content.replace("import { updateProfile, sendPasswordResetEmail } from 'firebase/auth';", "import { updateProfile, sendPasswordResetEmail, signInWithEmailAndPassword, createUserWithEmailAndPassword } from 'firebase/auth';")

auth_func_search = """  const handleAuth = (e: React.FormEvent) => {
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
      setUserName(name);
    } else {
      const savedName = localStorage.getItem('userName');
      if (savedName) setUserName(savedName);
    }
    
    setIsLoggedIn(true);
  };"""

auth_func_replace = """  const [isAuthenticating, setIsAuthenticating] = useState(false);

  const handleAuth = async (e: React.FormEvent) => {
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
    setIsAuthenticating(true);
    try {
      if (authMode === 'signup') {
        const userCredential = await createUserWithEmailAndPassword(auth, email, password);
        await updateProfile(userCredential.user, { displayName: name });
        // AuthContext will handle creating the user doc in Firestore
      } else {
        await signInWithEmailAndPassword(auth, email, password);
      }
    } catch (error: any) {
      console.error(error);
      setFormErrors([error.message || 'فشل تسجيل الدخول/الإنشاء']);
    } finally {
      setIsAuthenticating(false);
    }
  };"""

content = content.replace(auth_func_search, auth_func_replace)

# Now remove the fake logout
logout_func_search = """  const handleLogout = () => {
    localStorage.removeItem('isLoggedIn');
    setIsLoggedIn(false);
    alert("تم تسجيل الخروج بنجاح");
  };"""

logout_func_replace = """  const { logout } = useAuth();
  const handleLogout = async () => {
    try {
      await logout();
    } catch (e) {
      console.error(e);
    }
  };"""
content = content.replace(logout_func_search, logout_func_replace)

# Change isLoggedIn check to currentUser
content = content.replace("  if (!isLoggedIn) {", "  if (!currentUser) {")
content = content.replace("onClick={handleLogout}", "onClick={handleLogout}")

button_search = """            <button 
              type="submit" 
              className="w-full bg-yellow-500 hover:bg-yellow-400 text-black font-bold p-3 rounded-xl transition-colors shadow-[0_0_20px_rgba(234,179,8,0.3)] hover:shadow-[0_0_25px_rgba(234,179,8,0.5)]"
            >
              {authMode === 'login' ? 'دخول' : 'تسجيل حساب جديد'}
            </button>"""
            
button_replace = """            <button 
              type="submit" 
              disabled={isAuthenticating}
              className="w-full bg-yellow-500 hover:bg-yellow-400 text-black font-bold p-3 rounded-xl transition-colors shadow-[0_0_20px_rgba(234,179,8,0.3)] hover:shadow-[0_0_25px_rgba(234,179,8,0.5)] disabled:opacity-50"
            >
              {isAuthenticating ? 'يرجى الانتظار...' : (authMode === 'login' ? 'دخول' : 'تسجيل حساب جديد')}
            </button>"""
content = content.replace(button_search, button_replace)

with open("src/components/Profile.tsx", "w") as f:
    f.write(content)
