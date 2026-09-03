import re

with open("src/components/FanCommunity.tsx", "r") as f:
    content = f.read()

# 1. Add filter state
state_search = "const [commentText, setCommentText] = useState('');"
state_replace = """const [commentText, setCommentText] = useState('');
  const [activeFilter, setActiveFilter] = useState<'latest' | 'trending' | 'my'>('latest');

  // Filter and sort posts
  const displayPosts = [...posts]
    .sort((a, b) => {
      if (activeFilter === 'trending') return (b.likes + b.comments) - (a.likes + a.comments);
      return 0; // Default order is latest first since we prepend new posts
    })
    .filter(post => {
      if (activeFilter === 'my') return post.author === 'أنت';
      return true;
    });
"""
content = content.replace(state_search, state_replace)

# 2. Add UI for filters before Posts Feed
feed_search = "{/* Posts Feed */}"
feed_replace = """{/* Posts Filter Tabs */}
      <div className="flex gap-2 overflow-x-auto pb-2 scrollbar-hide">
        <button 
          onClick={() => setActiveFilter('latest')}
          className={`whitespace-nowrap px-4 py-2 rounded-full text-xs font-bold transition-colors border ${activeFilter === 'latest' ? 'bg-yellow-500 text-black border-yellow-500' : 'bg-zinc-900 text-zinc-400 border-zinc-800 hover:border-zinc-700 hover:text-white'}`}
        >
          أحدث المنشورات
        </button>
        <button 
          onClick={() => setActiveFilter('trending')}
          className={`whitespace-nowrap px-4 py-2 rounded-full text-xs font-bold transition-colors border ${activeFilter === 'trending' ? 'bg-yellow-500 text-black border-yellow-500' : 'bg-zinc-900 text-zinc-400 border-zinc-800 hover:border-zinc-700 hover:text-white'}`}
        >
          الأكثر تفاعلاً
        </button>
        <button 
          onClick={() => setActiveFilter('my')}
          className={`whitespace-nowrap px-4 py-2 rounded-full text-xs font-bold transition-colors border ${activeFilter === 'my' ? 'bg-yellow-500 text-black border-yellow-500' : 'bg-zinc-900 text-zinc-400 border-zinc-800 hover:border-zinc-700 hover:text-white'}`}
        >
          منشوراتي
        </button>
      </div>

      {/* Posts Feed */}"""
content = content.replace(feed_search, feed_replace)

# 3. Replace posts.map with displayPosts.map
content = content.replace("{posts.map(post => (", "{displayPosts.map(post => (")

with open("src/components/FanCommunity.tsx", "w") as f:
    f.write(content)

