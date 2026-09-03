import re

with open("src/components/FanCommunity.tsx", "r") as f:
    content = f.read()

# Replace storage imports with firebase imports
import_search = "import { readJSON, writeJSON } from '../lib/storage';"
import_replace = """import { collection, addDoc, updateDoc, doc, onSnapshot, query, orderBy } from 'firebase/firestore';
import { db } from '../lib/firebase';"""
content = content.replace(import_search, import_replace)

# Replace the DEFAULT_POSTS and useState with useEffect for Firestore
state_search = """  const DEFAULT_POSTS: Post[] = [
    {
      id: '1',
      author: 'أحمد الكاباوي',
      avatar: 'A',
      time: 'قبل ساعتين',
      content: 'أجواء رائعة اليوم في المدرجات! الفريق قدم أداء خرافي، النقاط الثلاث هي الأهم. الجراد الأصفر دائماً في الموعد 💛🖤',
      likes: 124,
      comments: 18,
      isLiked: false,
    },
    {
      id: '2',
      author: 'رياض 34',
      avatar: 'R',
      time: 'قبل 4 ساعات',
      content: 'صور من دخلة اليوم.. الإبداع مستمر!',
      imageUrl: 'https://images.unsplash.com/photo-1508344928928-7137b29de216?auto=format&fit=crop&q=80&w=800&h=400',
      likes: 342,
      comments: 45,
      isLiked: true,
    },
    {
      id: '3',
      author: 'وليد BBA',
      avatar: 'W',
      time: 'قبل 5 ساعات',
      content: 'من هو رجل المباراة برأيكم؟ بالنسبة لي الحارس كان سداً منيعاً.',
      likes: 89,
      comments: 112,
      isLiked: false,
    }
  ];

  const [posts, setPosts] = useState<Post[]>(() => {
    return readJSON('cabba-community-posts', DEFAULT_POSTS);
  });

  useEffect(() => {
    writeJSON('cabba-community-posts', posts);
  }, [posts]);"""

state_replace = """  const [posts, setPosts] = useState<Post[]>([]);

  useEffect(() => {
    const q = query(collection(db, 'posts'), orderBy('createdAt', 'desc'));
    const unsubscribe = onSnapshot(q, (snapshot) => {
      const postsData: Post[] = [];
      snapshot.forEach((doc) => {
        const data = doc.data();
        postsData.push({
          id: doc.id,
          author: data.author || 'مجهول',
          avatar: data.avatar || 'U',
          time: data.time || 'الآن',
          content: data.content || '',
          imageUrl: data.imageUrl,
          likes: data.likes || 0,
          comments: data.comments || 0,
          isLiked: false, // Local state
        });
      });
      setPosts(postsData);
    });

    return () => unsubscribe();
  }, []);"""
content = content.replace(state_search, state_replace)

# Replace handleAddComment
add_comment_search = """  const handleAddComment = (postId: string) => {
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
  };"""

add_comment_replace = """  const handleAddComment = async (postId: string) => {
    if (!commentText.trim()) return;
    try {
      const postRef = doc(db, 'posts', postId);
      const post = posts.find(p => p.id === postId);
      if (post) {
        await updateDoc(postRef, {
          comments: post.comments + 1
        });
      }
      setCommentText('');
      alert('تمت إضافة تعليقك بنجاح!');
    } catch (e) {
      console.error(e);
      alert('حدث خطأ');
    }
  };"""
content = content.replace(add_comment_search, add_comment_replace)

# Replace handleLike
like_search = """  const handleLike = (postId: string) => {
    setPosts(posts.map(post => {
      if (post.id === postId) {
        return {
          ...post,
          isLiked: !post.isLiked,
          likes: post.isLiked ? post.likes - 1 : post.likes + 1
        };
      }
      return post;
    }));
  };"""

like_replace = """  const handleLike = async (postId: string) => {
    const post = posts.find(p => p.id === postId);
    if (!post) return;
    
    // Optimistic local update for isLiked state
    setPosts(posts.map(p => {
      if (p.id === postId) {
        return { ...p, isLiked: !p.isLiked };
      }
      return p;
    }));

    try {
      const postRef = doc(db, 'posts', postId);
      await updateDoc(postRef, {
        likes: post.isLiked ? post.likes - 1 : post.likes + 1
      });
    } catch (e) {
      console.error(e);
      // Revert optimistic update
      setPosts(posts.map(p => {
        if (p.id === postId) {
          return { ...p, isLiked: post.isLiked };
        }
        return p;
      }));
    }
  };"""
content = content.replace(like_search, like_replace)

# Replace handlePost
post_search = """  const handlePost = () => {
    if (!newPostText.trim() && !newPostImage) return;
    
    const newPost: Post = {
      id: Date.now().toString(),
      author: 'أنت',
      avatar: 'Y',
      time: 'الآن',
      content: newPostText,
      imageUrl: newPostImage || undefined,
      likes: 0,
      comments: 0,
      isLiked: false,
    };
    
    setPosts([newPost, ...posts]);
    setNewPostText('');
    setNewPostImage(null);
  };"""

post_replace = """  const handlePost = async () => {
    if (!newPostText.trim() && !newPostImage) return;
    
    try {
      await addDoc(collection(db, 'posts'), {
        author: 'أنت',
        avatar: 'Y',
        time: 'الآن',
        content: newPostText,
        imageUrl: newPostImage || null,
        likes: 0,
        comments: 0,
        createdAt: Date.now()
      });
      
      setNewPostText('');
      setNewPostImage(null);
    } catch (e) {
      console.error(e);
      alert('حدث خطأ أثناء النشر');
    }
  };"""
content = content.replace(post_search, post_replace)

with open("src/components/FanCommunity.tsx", "w") as f:
    f.write(content)

