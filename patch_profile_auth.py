import re

with open("src/components/Profile.tsx", "r") as f:
    content = f.read()

import_search = "import { Settings, Shield, Edit2, LogOut, Info, Globe, ChevronLeft, X, CheckCircle2 } from 'lucide-react';"
import_replace = "import { Settings, Shield, Edit2, LogOut, Info, Globe, ChevronLeft, X, CheckCircle2 } from 'lucide-react';\nimport { useAuth } from '../contexts/AuthContext';"
content = content.replace(import_search, import_replace)

body_search = """export default function Profile() {
  const [activeModal, setActiveModal] = useState<'none' | 'profile' | 'language' | 'about'>('none');
  const [language, setLanguage] = useState<'ar' | 'fr' | 'en'>('ar');
  const fileInputRef = useRef<HTMLInputElement>(null);
  
  // Mock Data
  const [editName, setEditName] = useState('أحمد الكاباوي');
  const [editEmail, setEditEmail] = useState('ahmed@cabba.dz');
  const [userAvatar, setUserAvatar] = useState('https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=150&h=150&fit=crop');

  const handleLogout = () => {
    alert('تم تسجيل الخروج بنجاح');
  };"""

body_replace = """export default function Profile() {
  const { currentUser, userData, logout } = useAuth();
  const [activeModal, setActiveModal] = useState<'none' | 'profile' | 'language' | 'about'>('none');
  const [language, setLanguage] = useState<'ar' | 'fr' | 'en'>('ar');
  const fileInputRef = useRef<HTMLInputElement>(null);
  
  const [editName, setEditName] = useState(userData?.displayName || '');
  const [editEmail, setEditEmail] = useState(currentUser?.email || '');
  const [userAvatar, setUserAvatar] = useState(currentUser?.photoURL || 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=150&h=150&fit=crop');

  const handleLogout = async () => {
    try {
      await logout();
    } catch (e) {
      console.error('Logout error', e);
    }
  };"""
content = content.replace(body_search, body_replace)

ui_search = """        <div className="text-center">
          <h2 className="text-2xl font-bold text-white mb-1">أحمد الكاباوي</h2>
          <p className="text-zinc-400 text-sm mb-3">ahmed@cabba.dz</p>
          <div className="inline-flex items-center gap-1.5 bg-yellow-500/10 text-yellow-500 px-3 py-1 rounded-full border border-yellow-500/20">
            <Shield size={14} />
            <span className="text-xs font-bold">عضو بريميوم</span>
          </div>
        </div>"""
        
ui_replace = """        <div className="text-center">
          <h2 className="text-2xl font-bold text-white mb-1">{userData?.displayName || 'مشجع كاباوي'}</h2>
          <p className="text-zinc-400 text-sm mb-3">{currentUser?.email}</p>
          <div className="inline-flex items-center gap-1.5 bg-yellow-500/10 text-yellow-500 px-3 py-1 rounded-full border border-yellow-500/20">
            <Shield size={14} />
            <span className="text-xs font-bold capitalize">{userData?.role === 'admin' ? 'مدير (Admin)' : userData?.role === 'member' ? 'عضو رسمي' : 'مشجع عادي'}</span>
          </div>
        </div>"""
content = content.replace(ui_search, ui_replace)

with open("src/components/Profile.tsx", "w") as f:
    f.write(content)

