import re

with open("src/components/FanCommunity.tsx", "r") as f:
    content = f.read()

import_search = "import { collection, addDoc, onSnapshot, query, orderBy, doc, updateDoc } from 'firebase/firestore';"
import_replace = "import { collection, addDoc, onSnapshot, query, orderBy, doc, updateDoc, deleteDoc } from 'firebase/firestore';\nimport { Trash2 } from 'lucide-react';"
content = content.replace(import_search, import_replace)

delete_handler = """  const handleDeletePost = async (postId: string, authorId?: string) => {
    if (authorId !== currentUser?.uid && userData?.role !== 'admin') return;
    if (!window.confirm('حذف المنشور؟')) return;
    try {
      await deleteDoc(doc(db, 'posts', postId));
    } catch (e) {
      console.error(e);
      alert('خطأ في حذف المنشور');
    }
  };
"""

body_search = "  const handleLike = async (postId: string, currentLikes: number) => {"
body_replace = delete_handler + "\n" + body_search
content = content.replace(body_search, body_replace)

ui_search = """                <div className="flex justify-between items-start mb-4">
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 rounded-full bg-gradient-to-br from-zinc-700 to-zinc-800 flex items-center justify-center font-bold text-lg border border-zinc-700">
                      {post.avatar}
                    </div>
                    <div>
                      <h4 className="font-bold text-white text-sm">{post.author}</h4>
                      <p className="text-xs text-zinc-500">{post.time}</p>
                    </div>
                  </div>
                </div>"""

ui_replace = """                <div className="flex justify-between items-start mb-4">
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 rounded-full bg-gradient-to-br from-zinc-700 to-zinc-800 flex items-center justify-center font-bold text-lg border border-zinc-700 overflow-hidden">
                      {post.authorId === currentUser?.uid && currentUser?.photoURL ? (
                        <img src={currentUser.photoURL} className="w-full h-full object-cover" alt="avatar" />
                      ) : (
                        post.avatar
                      )}
                    </div>
                    <div>
                      <h4 className="font-bold text-white text-sm">{post.author}</h4>
                      <p className="text-xs text-zinc-500">{post.time}</p>
                    </div>
                  </div>
                  {(post.authorId === currentUser?.uid || userData?.role === 'admin') && (
                    <button onClick={() => handleDeletePost(post.id, post.authorId)} className="text-red-500 hover:text-red-400 p-1">
                      <Trash2 size={16} />
                    </button>
                  )}
                </div>"""
content = content.replace(ui_search, ui_replace)

with open("src/components/FanCommunity.tsx", "w") as f:
    f.write(content)

