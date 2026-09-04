import re

with open("src/components/Profile.tsx", "r") as f:
    content = f.read()

import_search = "import { useAuth } from '../contexts/AuthContext';"
import_replace = "import { useAuth } from '../contexts/AuthContext';\nimport { ref, uploadString, getDownloadURL } from 'firebase/storage';\nimport { doc, updateDoc } from 'firebase/firestore';\nimport { updateProfile } from 'firebase/auth';\nimport { auth, storage } from '../lib/firebase';"
content = content.replace(import_search, import_replace)

save_search = """  const handleSaveProfile = () => {
    // In a real app we'd update Firestore and Auth profile
    alert('سيتم إضافة ميزة تعديل الملف الشخصي قريباً');
    setActiveModal('none');
  };"""
  
save_replace = """  const [isSaving, setIsSaving] = useState(false);
  
  const handleSaveProfile = async () => {
    if (!currentUser) return;
    setIsSaving(true);
    try {
      let finalAvatar = userAvatar;
      if (userAvatar.startsWith('data:image')) {
        const imageRef = ref(storage, `avatars/${currentUser.uid}_${Date.now()}`);
        await uploadString(imageRef, userAvatar, 'data_url');
        finalAvatar = await getDownloadURL(imageRef);
        setUserAvatar(finalAvatar);
      }

      await updateProfile(currentUser, {
        displayName: editName,
        photoURL: finalAvatar
      });
      
      const userRef = doc(db, 'users', currentUser.uid);
      await updateDoc(userRef, {
        displayName: editName,
        photoURL: finalAvatar
      });

      setUserName(editName);
      alert('تم حفظ التعديلات بنجاح!');
      setActiveModal('none');
    } catch (error) {
      console.error(error);
      alert('حدث خطأ أثناء الحفظ');
    } finally {
      setIsSaving(false);
    }
  };"""
content = content.replace(save_search, save_replace)

button_search = """                  <button 
                    onClick={handleSaveProfile}
                    className="w-full bg-yellow-500 hover:bg-yellow-400 text-black font-bold p-3 rounded-xl transition-colors mt-2"
                  >
                    حفظ التغييرات
                  </button>"""
                  
button_replace = """                  <button 
                    onClick={handleSaveProfile}
                    disabled={isSaving}
                    className="w-full bg-yellow-500 hover:bg-yellow-400 text-black font-bold p-3 rounded-xl transition-colors mt-2 disabled:opacity-50"
                  >
                    {isSaving ? 'جاري الحفظ...' : 'حفظ التغييرات'}
                  </button>"""
content = content.replace(button_search, button_replace)

with open("src/components/Profile.tsx", "w") as f:
    f.write(content)

