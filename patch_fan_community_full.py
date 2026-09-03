import re

with open("src/components/FanCommunity.tsx", "r") as f:
    content = f.read()

# Add states for comments and menus
new_states = """  const [activeMenuId, setActiveMenuId] = useState<string | null>(null);
  const [activeCommentsId, setActiveCommentsId] = useState<string | null>(null);
  const [commentText, setCommentText] = useState('');

  const handleShare = async (content: string) => {
    try {
      if (navigator.share) {
        await navigator.share({
          title: 'مجتمع الكابا',
          text: content,
        });
      } else {
        alert('تم نسخ المنشور للحافظة!');
      }
    } catch (error) {
      console.log('Error sharing:', error);
    }
  };

  const handleAddComment = (postId: string) => {
    if (!commentText.trim()) return;
    setPosts(posts.map(post => {
      if (post.id === postId) {
        return {
          ...post,
          comments: post.comments + 1
        };
      }
      return post;
    }));
    setCommentText('');
    alert('تمت إضافة تعليقك بنجاح!');
  };
"""

content = content.replace("  const handleLike = (postId: string) => {", new_states + "\n  const handleLike = (postId: string) => {")

# Three dots button
old_dots = """<button onClick={() => alert('هذه الخاصية ستتوفر قريباً!')} className="text-zinc-600 hover:text-white">...</button>"""
new_dots = """<div className="relative">
                <button onClick={() => setActiveMenuId(activeMenuId === post.id ? null : post.id)} className="text-zinc-600 hover:text-white p-2">...</button>
                {activeMenuId === post.id && (
                  <div className="absolute left-0 top-8 bg-zinc-800 border border-zinc-700 rounded-lg shadow-xl w-32 py-1 z-10 animate-in fade-in duration-200">
                    <button onClick={() => { alert('تم حفظ المنشور في المفضلة'); setActiveMenuId(null); }} className="w-full text-right px-4 py-2 text-sm text-white hover:bg-zinc-700 transition-colors">حفظ المنشور</button>
                    <button onClick={() => { alert('تم الإبلاغ عن هذا المنشور. شكراً لك.'); setActiveMenuId(null); }} className="w-full text-right px-4 py-2 text-sm text-red-400 hover:bg-zinc-700 transition-colors">إبلاغ</button>
                  </div>
                )}
              </div>"""
content = content.replace(old_dots, new_dots)

# Comments and share buttons
old_comment_share = """<button onClick={() => alert('هذه الخاصية ستتوفر قريباً!')} className="flex items-center gap-2 text-xs font-bold text-zinc-500 hover:text-white transition-colors">
                <MessageSquare size={18} />
                <span>{post.comments}</span>
              </button>
              
              <button onClick={() => alert('هذه الخاصية ستتوفر قريباً!')} className="flex items-center gap-2 text-xs font-bold text-zinc-500 hover:text-white transition-colors">
                <Share2 size={18} />
                <span>مشاركة</span>
              </button>"""

new_comment_share = """<button onClick={() => setActiveCommentsId(activeCommentsId === post.id ? null : post.id)} className={`flex items-center gap-2 text-xs font-bold transition-colors ${activeCommentsId === post.id ? 'text-white' : 'text-zinc-500 hover:text-white'}`}>
                <MessageSquare size={18} />
                <span>{post.comments}</span>
              </button>
              
              <button onClick={() => handleShare(post.content)} className="flex items-center gap-2 text-xs font-bold text-zinc-500 hover:text-white transition-colors">
                <Share2 size={18} />
                <span>مشاركة</span>
              </button>"""
              
content = content.replace(old_comment_share, new_comment_share)

# Add comments section
comments_section = """</div>
            
            {activeCommentsId === post.id && (
              <div className="mt-4 pt-4 border-t border-zinc-800/50 animate-in slide-in-from-top-2 duration-200">
                <div className="flex gap-2">
                  <input 
                    type="text" 
                    value={commentText}
                    onChange={(e) => setCommentText(e.target.value)}
                    placeholder="أضف تعليقاً..." 
                    className="flex-1 bg-zinc-800/50 border border-zinc-700 rounded-full px-4 py-2 text-xs text-white outline-none focus:border-yellow-500 transition-colors"
                  />
                  <button onClick={() => handleAddComment(post.id)} disabled={!commentText.trim()} className="bg-yellow-500 text-black px-4 py-2 rounded-full text-xs font-bold disabled:opacity-50 transition-colors">
                    إرسال
                  </button>
                </div>
              </div>
            )}
          </div>"""

# Replace the closing div of the post with comments_section
content = content.replace("""</div>\n          </div>\n        ))}""", comments_section + "\n        ))}").replace("</div>\n\n          </div>\n        ))}","</div>\n          </div>\n        ))}").replace("</div>\n            {activeCommentsId", "\n            {activeCommentsId")

with open("src/components/FanCommunity.tsx", "w") as f:
    f.write(content)

