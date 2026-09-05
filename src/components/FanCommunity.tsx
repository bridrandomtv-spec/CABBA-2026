import { useState, useRef, useEffect } from 'react';
import { collection, addDoc, updateDoc, doc, onSnapshot, query, orderBy } from 'firebase/firestore';
import { db, storage } from '../lib/firebase';
import { ref, uploadString, getDownloadURL } from 'firebase/storage';
import { useAuth } from '../contexts/AuthContext';
import { Heart, MessageSquare, Share2, Image as ImageIcon, Send, User, X } from 'lucide-react';

interface Post {
  id: string;
  authorId?: string;
  author: string;
  avatar: string;
  time: string;
  content: string;
  imageUrl?: string;
  likes: number;
  comments: number;
  isLiked: boolean;
}

export default function FanCommunity() {
  const { currentUser, userData } = useAuth();
  const [posts, setPosts] = useState<Post[]>([]);
  const [isUploading, setIsUploading] = useState(false);

  useEffect(() => {
    const q = query(collection(db, 'posts'), orderBy('createdAt', 'desc'));
    const unsubscribe = onSnapshot(q, (snapshot) => {
      const postsData: Post[] = [];
      snapshot.forEach((doc) => {
        const data = doc.data();
        postsData.push({
          id: doc.id,
          authorId: data.authorId,
          author: data.author || 'مجهول',
          avatar: data.avatar || 'U',
          time: data.time || 'الآن',
          content: data.content || '',
          imageUrl: data.imageUrl,
          likes: data.likes || 0,
          comments: data.comments || 0,
          isLiked: data.isLiked || false,
        });
      });
      setPosts(postsData);
    });

    return () => unsubscribe();
  }, []);

  const [newPostText, setNewPostText] = useState('');
  const [newPostImage, setNewPostImage] = useState<string | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleImageUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (event) => {
      const img = new Image();
      img.onload = () => {
        const canvas = document.createElement('canvas');
        let width = img.width;
        let height = img.height;
        
        const MAX_DIMENSION = 800;
        if (width > height && width > MAX_DIMENSION) {
          height *= MAX_DIMENSION / width;
          width = MAX_DIMENSION;
        } else if (height > MAX_DIMENSION) {
          width *= MAX_DIMENSION / height;
          height = MAX_DIMENSION;
        }

        canvas.width = width;
        canvas.height = height;
        const ctx = canvas.getContext('2d');
        ctx?.drawImage(img, 0, 0, width, height);
        
        setNewPostImage(canvas.toDataURL('image/jpeg', 0.6));
      };
      img.src = event.target?.result as string;
    };
    reader.readAsDataURL(file);
  };

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
        authorId: currentUser?.id || '',
        author: userData?.displayName || currentUser?.displayName || 'مشجع البرج',
        avatar: currentUser?.avatarUrl || 'https://api.dicebear.com/7.x/avataaars/svg?seed=cabba&backgroundColor=f59e0b',
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
    } finally {
      setIsUploading(false);
    }
  };

  const toggleLike = async (postId: string) => {
    const post = posts.find(p => p.id === postId);
    if (!post) return;
    try {
      await updateDoc(doc(db, 'posts', postId), {
        likes: post.isLiked ? post.likes - 1 : post.likes + 1,
        isLiked: !post.isLiked
      });
    } catch(e) {}
  };

  return (
    <div className="flex flex-col h-full bg-zinc-950" dir="rtl">


      <div className="flex-1 overflow-y-auto hide-scrollbar pb-24">
        
          <div className="p-4 space-y-6">
            
            {/* Create Post */}
            <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-4 shadow-sm relative z-10">
              <div className="flex gap-3 mb-3">
                <div className="w-10 h-10 bg-zinc-800 rounded-full flex items-center justify-center border border-zinc-700 flex-shrink-0">
                   {currentUser?.avatarUrl ? <img src={currentUser.avatarUrl} alt="Avatar" className="w-full h-full rounded-full" /> : <User size={20} className="text-zinc-500" />}
                </div>
                <textarea 
                  value={newPostText}
                  onChange={(e) => setNewPostText(e.target.value)}
                  placeholder="شارك أفكارك مع العائلة الصفراء..."
                  className="w-full bg-transparent border-none text-white focus:outline-none resize-none h-10 placeholder:text-zinc-600 text-sm py-2"
                />
              </div>
              
              {newPostImage && (
                <div className="relative mb-3 rounded-xl overflow-hidden border border-zinc-800">
                  <img src={newPostImage} alt="Preview" className="w-full max-h-48 object-cover" />
                  <button 
                    onClick={() => setNewPostImage(null)}
                    className="absolute top-2 right-2 bg-black/50 text-white p-1 rounded-full hover:bg-red-500 transition-colors"
                  >
                    <X size={16} />
                  </button>
                </div>
              )}
              
              <div className="flex justify-between items-center border-t border-zinc-800 pt-3">
                <div className="flex gap-2">
                  <input 
                    type="file" 
                    accept="image/*" 
                    ref={fileInputRef} 
                    className="hidden" 
                    onChange={handleImageUpload} 
                  />
                  <button 
                    onClick={() => fileInputRef.current?.click()} 
                    className="text-zinc-500 hover:text-yellow-500 transition-colors p-2 rounded-full hover:bg-zinc-800/50"
                  >
                    <ImageIcon size={20} />
                  </button>
                </div>
                <button 
                  onClick={handlePost}
                  disabled={(!newPostText.trim() && !newPostImage) || isUploading}
                  className="bg-yellow-500 hover:bg-yellow-400 text-black px-4 py-1.5 rounded-full text-xs font-bold flex items-center gap-2 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  <span>{isUploading ? 'جاري النشر...' : 'نشر'}</span>
                  {!isUploading && <Send size={14} className="rotate-180" />}
                </button>
              </div>
            </div>

            {/* Posts List */}
            <div className="space-y-4">
              {posts.map(post => (
                <div key={post.id} className="bg-zinc-900 border border-zinc-800 rounded-2xl p-4 shadow-sm relative z-10">
                  <div className="flex justify-between items-start mb-3">
                    <div className="flex items-center gap-3">
                      <div className="w-10 h-10 bg-zinc-800 rounded-full flex items-center justify-center border border-yellow-500/30">
                        {post.avatar && post.avatar !== 'U' ? (
                          <img src={post.avatar} alt={post.author} className="w-full h-full rounded-full" />
                        ) : (
                          <span className="font-bold text-yellow-500">{post.author.charAt(0)}</span>
                        )}
                      </div>
                      <div>
                        <h4 className="font-bold text-white text-sm">{post.author}</h4>
                        <p className="text-[10px] text-zinc-500">{post.time}</p>
                      </div>
                    </div>
                  </div>
                  
                  <p className="text-zinc-300 text-sm mb-3 leading-relaxed">
                    {post.content}
                  </p>
                  
                  {post.imageUrl && (
                    <div className="rounded-xl overflow-hidden mb-3 border border-zinc-800 max-h-64">
                      <img src={post.imageUrl} alt="Post media" className="w-full h-full object-cover" />
                    </div>
                  )}
                  
                  <div className="flex items-center gap-6 border-t border-zinc-800 pt-3 mt-2">
                    <button 
                      onClick={() => toggleLike(post.id)}
                      className={`flex items-center gap-1.5 text-xs font-bold transition-colors ${post.isLiked ? 'text-red-500' : 'text-zinc-500 hover:text-red-400'}`}
                    >
                      <Heart size={16} className={post.isLiked ? 'fill-current' : ''} />
                      <span>{post.likes}</span>
                    </button>
                    <button className="flex items-center gap-1.5 text-xs font-bold text-zinc-500 hover:text-white transition-colors">
                      <MessageSquare size={16} />
                      <span>{post.comments}</span>
                    </button>
                  </div>
                </div>
              ))}
            </div>
          </div>
      </div>
    </div>
  );
}
