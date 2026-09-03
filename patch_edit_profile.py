import re

with open("src/components/Profile.tsx", "r") as f:
    content = f.read()

# Fix imports
content = content.replace("import { useState } from 'react';", "import { useState, useRef } from 'react';")

# Fix handleAuth email saving
handle_auth_save = """    // Save mock user data
    if (authMode === 'signup') {
      localStorage.setItem('userName', name);
    }
    setIsLoggedIn(true);"""

new_handle_auth_save = """    // Save mock user data
    if (authMode === 'signup') {
      localStorage.setItem('userName', name);
      setUserName(name);
    }
    localStorage.setItem('userEmail', email);
    setUserEmail(email);
    setIsLoggedIn(true);"""

content = content.replace(handle_auth_save, new_handle_auth_save)

# Replace old userName const and add states
old_user_name = "  const userName = localStorage.getItem('userName') || 'أمين. ب';"
new_states = """  const [userName, setUserName] = useState(() => localStorage.getItem('userName') || 'أمين. ب');
  const [userEmail, setUserEmail] = useState(() => localStorage.getItem('userEmail') || 'supporter@cabba.dz');
  const [userAvatar, setUserAvatar] = useState(() => localStorage.getItem('userAvatar') || `https://api.dicebear.com/7.x/avataaars/svg?seed=Amine&backgroundColor=f59e0b`);
  
  const [editName, setEditName] = useState(userName);
  const [editEmail, setEditEmail] = useState(userEmail);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleImageUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        const base64String = reader.result as string;
        setUserAvatar(base64String);
        localStorage.setItem('userAvatar', base64String);
      };
      reader.readAsDataURL(file);
    }
  };

  const handleSaveProfile = () => {
    localStorage.setItem('userName', editName);
    localStorage.setItem('userEmail', editEmail);
    setUserName(editName);
    setUserEmail(editEmail);
    alert('تم حفظ التعديلات بنجاح!');
    setActiveModal('none');
  };
"""
content = content.replace(old_user_name, new_states)

# Fix the profile UI avatar rendering (Digital Membership Card section)
old_avatar_html = '<img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Amine&backgroundColor=f59e0b" alt={`صورة ${userName}`} className="w-full h-full object-cover" />'
new_avatar_html = '<img src={userAvatar} alt={`صورة ${userName}`} className="w-full h-full object-cover" />'
content = content.replace(old_avatar_html, new_avatar_html)

# Fix the profile Edit Modal
old_profile_modal = """              {activeModal === 'profile' && (
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
              )}"""

new_profile_modal = """              {activeModal === 'profile' && (
                <div className="space-y-4">
                  <div className="flex flex-col items-center mb-6">
                    <div className="w-20 h-20 rounded-full bg-zinc-800 border-2 border-yellow-500 overflow-hidden shadow-lg mb-3">
                      <img src={userAvatar} alt="Avatar" className="w-full h-full object-cover" />
                    </div>
                    <input 
                      type="file" 
                      accept="image/*" 
                      ref={fileInputRef} 
                      className="hidden" 
                      onChange={handleImageUpload} 
                    />
                    <button onClick={() => fileInputRef.current?.click()} className="text-xs text-yellow-500 font-bold hover:underline">
                      تغيير الصورة
                    </button>
                  </div>
                  <div className="space-y-2">
                    <label className="text-xs font-bold text-zinc-400">الاسم الكامل</label>
                    <input 
                      type="text" 
                      value={editName}
                      onChange={(e) => setEditName(e.target.value)}
                      className="w-full bg-zinc-800 border border-zinc-700 rounded-xl p-3 text-white text-right focus:outline-none focus:border-yellow-500 transition-colors" 
                    />
                  </div>
                  <div className="space-y-2">
                    <label className="text-xs font-bold text-zinc-400">البريد الإلكتروني</label>
                    <input 
                      type="email" 
                      value={editEmail}
                      onChange={(e) => setEditEmail(e.target.value)}
                      className="w-full bg-zinc-800 border border-zinc-700 rounded-xl p-3 text-white text-right focus:outline-none focus:border-yellow-500 transition-colors" 
                    />
                  </div>
                  <button 
                    onClick={handleSaveProfile}
                    className="w-full bg-yellow-500 hover:bg-yellow-400 text-black font-bold p-3 rounded-xl transition-colors mt-2"
                  >
                    حفظ التغييرات
                  </button>
                </div>
              )}"""

content = content.replace(old_profile_modal, new_profile_modal)

with open("src/components/Profile.tsx", "w") as f:
    f.write(content)

