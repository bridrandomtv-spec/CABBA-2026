import re

with open("src/components/Profile.tsx", "r") as f:
    content = f.read()

# Make sure X is imported from lucide-react
if " X," not in content and "{ X " not in content:
    content = content.replace("import { Award,", "import { Award, X,")

# Add the activeModal state
hooks_insertion = """  const [activeModal, setActiveModal] = useState<'none' | 'profile' | 'language' | 'about'>('none');
"""
content = content.replace("  const userName = localStorage.getItem('userName') || 'أمين. ب';", "  const userName = localStorage.getItem('userName') || 'أمين. ب';\n" + hooks_insertion)

# Replace the buttons
settings_buttons = """        <button 
          onClick={() => alert("قريباً: تعديل الملف الشخصي")}
          className="w-full bg-zinc-900 hover:bg-zinc-800 border border-zinc-800/50 p-4 rounded-xl flex items-center justify-between transition-colors"
        >
          <span className="text-sm text-white font-medium">الملف الشخصي</span>
          <ChevronLeft size={16} className="text-zinc-600" />
        </button>

        <NotificationSettings />

        <button 
          onClick={() => alert("العربية هي اللغة الوحيدة المتاحة حالياً.")}
          className="w-full bg-zinc-900 hover:bg-zinc-800 border border-zinc-800/50 p-4 rounded-xl flex items-center justify-between transition-colors"
        >
          <span className="text-sm text-white font-medium">اللغة (العربية)</span>
          <ChevronLeft size={16} className="text-zinc-600" />
        </button>

        <button 
          onClick={() => alert("تطبيق أنصار شباب أهلي برج بوعريريج - الإصدار 1.0")}
          className="w-full bg-zinc-900 hover:bg-zinc-800 border border-zinc-800/50 p-4 rounded-xl flex items-center justify-between transition-colors"
        >
          <span className="text-sm text-white font-medium">عن التطبيق</span>
          <ChevronLeft size={16} className="text-zinc-600" />
        </button>"""

new_settings_buttons = """        <button 
          onClick={() => setActiveModal('profile')}
          className="w-full bg-zinc-900 hover:bg-zinc-800 border border-zinc-800/50 p-4 rounded-xl flex items-center justify-between transition-colors group"
        >
          <span className="text-sm text-white font-medium group-hover:text-yellow-500 transition-colors">تعديل الملف الشخصي</span>
          <ChevronLeft size={16} className="text-zinc-600 group-hover:text-yellow-500 transition-colors" />
        </button>

        <NotificationSettings />

        <button 
          onClick={() => setActiveModal('language')}
          className="w-full bg-zinc-900 hover:bg-zinc-800 border border-zinc-800/50 p-4 rounded-xl flex items-center justify-between transition-colors group"
        >
          <span className="text-sm text-white font-medium group-hover:text-yellow-500 transition-colors">إعدادات اللغة</span>
          <ChevronLeft size={16} className="text-zinc-600 group-hover:text-yellow-500 transition-colors" />
        </button>

        <button 
          onClick={() => setActiveModal('about')}
          className="w-full bg-zinc-900 hover:bg-zinc-800 border border-zinc-800/50 p-4 rounded-xl flex items-center justify-between transition-colors group"
        >
          <span className="text-sm text-white font-medium group-hover:text-yellow-500 transition-colors">عن التطبيق</span>
          <ChevronLeft size={16} className="text-zinc-600 group-hover:text-yellow-500 transition-colors" />
        </button>"""

content = content.replace(settings_buttons, new_settings_buttons)

# Add modals rendering at the end of the return statement before the final </div>
modals_rendering = """
      {/* Modals for Settings */}
      {activeModal !== 'none' && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm animate-in fade-in duration-200">
          <div className="bg-zinc-900 border border-yellow-500/30 rounded-3xl w-full max-w-sm overflow-hidden shadow-[0_10px_40px_rgba(234,179,8,0.1)] flex flex-col max-h-[80vh]">
            <div className="flex justify-between items-center p-4 border-b border-zinc-800">
              <h3 className="font-bold text-white text-lg">
                {activeModal === 'profile' && 'تعديل الملف الشخصي'}
                {activeModal === 'language' && 'اللغة (Language)'}
                {activeModal === 'about' && 'عن التطبيق'}
              </h3>
              <button 
                onClick={() => setActiveModal('none')}
                className="p-2 bg-zinc-800 hover:bg-zinc-700 text-zinc-400 hover:text-white rounded-full transition-colors"
              >
                <X size={20} />
              </button>
            </div>
            
            <div className="p-6 overflow-y-auto">
              {activeModal === 'profile' && (
                <div className="space-y-4">
                  <div className="flex flex-col items-center mb-6">
                    <div className="w-20 h-20 rounded-full bg-zinc-800 border-2 border-yellow-500 overflow-hidden shadow-lg mb-3">
                      <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Amine&backgroundColor=f59e0b" alt="Avatar" className="w-full h-full object-cover" />
                    </div>
                    <button className="text-xs text-yellow-500 font-bold hover:underline">تغيير الصورة</button>
                  </div>
                  <div className="space-y-2">
                    <label className="text-xs font-bold text-zinc-400">الاسم الكامل</label>
                    <input type="text" defaultValue={userName} className="w-full bg-zinc-800 border border-zinc-700 rounded-xl p-3 text-white text-right focus:outline-none focus:border-yellow-500 transition-colors" />
                  </div>
                  <div className="space-y-2">
                    <label className="text-xs font-bold text-zinc-400">البريد الإلكتروني</label>
                    <input type="email" defaultValue="supporter@cabba.dz" className="w-full bg-zinc-800 border border-zinc-700 rounded-xl p-3 text-white text-right focus:outline-none focus:border-yellow-500 transition-colors" />
                  </div>
                  <button 
                    onClick={() => {
                      alert('تم حفظ التعديلات بنجاح!');
                      setActiveModal('none');
                    }}
                    className="w-full bg-yellow-500 hover:bg-yellow-400 text-black font-bold p-3 rounded-xl transition-colors mt-2"
                  >
                    حفظ التغييرات
                  </button>
                </div>
              )}

              {activeModal === 'language' && (
                <div className="space-y-3">
                  <button className="w-full bg-zinc-800 border-2 border-yellow-500 p-4 rounded-xl flex items-center justify-between">
                    <span className="font-bold text-white">العربية (Arabic)</span>
                    <CheckCircle2 size={20} className="text-yellow-500" />
                  </button>
                  <button className="w-full bg-zinc-800/50 border-2 border-transparent p-4 rounded-xl flex items-center justify-between opacity-50 cursor-not-allowed">
                    <span className="font-bold text-white">الفرنسية (Français)</span>
                    <span className="text-xs text-zinc-500">قريباً</span>
                  </button>
                  <button className="w-full bg-zinc-800/50 border-2 border-transparent p-4 rounded-xl flex items-center justify-between opacity-50 cursor-not-allowed">
                    <span className="font-bold text-white">الإنجليزية (English)</span>
                    <span className="text-xs text-zinc-500">قريباً</span>
                  </button>
                </div>
              )}

              {activeModal === 'about' && (
                <div className="text-center space-y-6">
                  <div className="w-24 h-24 mx-auto bg-gradient-to-br from-yellow-400 to-yellow-600 rounded-full flex items-center justify-center border-4 border-zinc-800 shadow-[0_0_30px_rgba(234,179,8,0.3)]">
                    <span className="font-bold text-black text-5xl">C</span>
                  </div>
                  <div>
                    <h4 className="font-bold text-white text-xl mb-1">CABBA Supporters</h4>
                    <p className="text-yellow-500 font-bold text-sm">الإصدار 1.0.0</p>
                  </div>
                  <div className="bg-zinc-800/50 rounded-xl p-4 text-xs text-zinc-400 leading-relaxed text-center space-y-3">
                    <p>التطبيق الرسمي لأنصار أهلي برج بوعريريج.</p>
                    <p>تم تطويره بحب للجراد الأصفر، ليجمع العائلة الصفراء في منصة رقمية واحدة.</p>
                    <p>© 2026 جميع الحقوق محفوظة.</p>
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      )}
"""

content = content.replace("    </div>\n  );\n}", modals_rendering + "    </div>\n  );\n}")

with open("src/components/Profile.tsx", "w") as f:
    f.write(content)
