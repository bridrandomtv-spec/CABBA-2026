import re

with open("src/components/FanCommunity.tsx", "r") as f:
    content = f.read()

import_search = "import { db } from '../lib/firebase';"
import_replace = "import { db, storage } from '../lib/firebase';\nimport { ref, uploadString, getDownloadURL } from 'firebase/storage';"
content = content.replace(import_search, import_replace)

# Modify handlePost
handlepost_search = """  const handlePost = async () => {
    if (!newPostText.trim() && !newPostImage) return;
    
    try {
      await addDoc(collection(db, 'posts'), {
        authorId: currentUser?.uid || '',
        author: userData?.name || currentUser?.displayName || 'مشجع البرج',
        avatar: currentUser?.photoURL || 'https://api.dicebear.com/7.x/avataaars/svg?seed=cabba&backgroundColor=f59e0b',
        time: 'الآن',
        content: newPostText,
        imageUrl: newPostImage || null,
        likes: 0,
        comments: 0,
        createdAt: Date.now(),
        isLiked: false
      });
      setNewPostText('');
      setNewPostImage('');
    } catch (error) {
      console.error(error);
      alert('حدث خطأ أثناء النشر');
    }
  };"""

handlepost_replace = """  const [isUploading, setIsUploading] = useState(false);
  const handlePost = async () => {
    if (!newPostText.trim() && !newPostImage) return;
    setIsUploading(true);
    
    try {
      let finalImageUrl = null;
      if (newPostImage) {
        if (newPostImage.startsWith('data:image')) {
          const imageRef = ref(storage, `community/${Date.now()}_${Math.random().toString(36).substring(7)}`);
          await uploadString(imageRef, newPostImage, 'data_url');
          finalImageUrl = await getDownloadURL(imageRef);
        } else {
          finalImageUrl = newPostImage;
        }
      }
      
      await addDoc(collection(db, 'posts'), {
        authorId: currentUser?.uid || '',
        author: userData?.displayName || currentUser?.displayName || 'مشجع البرج',
        avatar: currentUser?.photoURL || 'https://api.dicebear.com/7.x/avataaars/svg?seed=cabba&backgroundColor=f59e0b',
        time: 'الآن',
        content: newPostText,
        imageUrl: finalImageUrl,
        likes: 0,
        comments: 0,
        createdAt: Date.now(),
        isLiked: false
      });
      setNewPostText('');
      setNewPostImage('');
    } catch (error) {
      console.error(error);
      alert('حدث خطأ أثناء النشر');
    } finally {
      setIsUploading(false);
    }
  };"""
content = content.replace(handlepost_search, handlepost_replace)

button_search = """              <button 
                onClick={handlePost}
                disabled={!newPostText.trim() && !newPostImage}
                className="bg-yellow-500 hover:bg-yellow-400 text-black px-4 py-1.5 rounded-full text-xs font-bold flex items-center gap-2 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <span>نشر</span>
                <Send size={14} className="rotate-180" />
              </button>"""
              
button_replace = """              <button 
                onClick={handlePost}
                disabled={(!newPostText.trim() && !newPostImage) || isUploading}
                className="bg-yellow-500 hover:bg-yellow-400 text-black px-4 py-1.5 rounded-full text-xs font-bold flex items-center gap-2 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <span>{isUploading ? 'جاري النشر...' : 'نشر'}</span>
                {!isUploading && <Send size={14} className="rotate-180" />}
              </button>"""
content = content.replace(button_search, button_replace)

content = content.replace("userData?.name", "userData?.displayName")

with open("src/components/FanCommunity.tsx", "w") as f:
    f.write(content)

