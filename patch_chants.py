import re

with open("src/components/ChantsLibrary.tsx", "r") as f:
    content = f.read()

import_search = "import { Play, Pause, Heart, Search, Filter, Music } from 'lucide-react';"
import_replace = "import { Play, Pause, Heart, Search, Filter, Music } from 'lucide-react';\nimport { useState, useEffect } from 'react';\nimport { collection, query, orderBy, onSnapshot, doc, updateDoc, increment } from 'firebase/firestore';\nimport { db } from '../lib/firebase';\nimport { Chant } from './admin/AdminChants';"
content = content.replace(import_search, import_replace)

body_search = """export default function ChantsLibrary() {
  const [activeCategory, setActiveCategory] = useState('all');
  const [searchQuery, setSearchQuery] = useState('');
  const [playing, setPlaying] = useState<number | null>(null);"""
  
body_replace = """export default function ChantsLibrary() {
  const [chants, setChants] = useState<Chant[]>([]);
  const [activeCategory, setActiveCategory] = useState('all');
  const [searchQuery, setSearchQuery] = useState('');
  const [playing, setPlaying] = useState<string | null>(null);
  const [audioElement, setAudioElement] = useState<HTMLAudioElement | null>(null);

  useEffect(() => {
    const q = query(collection(db, 'chants'), orderBy('createdAt', 'desc'));
    const un = onSnapshot(q, (snapshot) => {
      const data: Chant[] = [];
      snapshot.forEach(doc => data.push({ id: doc.id, ...doc.data() } as Chant));
      setChants(data);
    });
    return () => {
      un();
      if (audioElement) {
        audioElement.pause();
      }
    };
  }, []);

  const handlePlay = async (chant: Chant) => {
    if (!chant.audioUrl) return;
    
    if (playing === chant.id) {
      audioElement?.pause();
      setPlaying(null);
    } else {
      if (audioElement) {
        audioElement.pause();
      }
      const audio = new Audio(chant.audioUrl);
      audio.play().catch(e => console.error("Error playing audio", e));
      setAudioElement(audio);
      setPlaying(chant.id);
      
      // Increment views
      try {
        await updateDoc(doc(db, 'chants', chant.id), { views: increment(1) });
      } catch(e) {}
    }
  };
"""
content = content.replace(body_search, body_replace)

ui_search = """        <div className="space-y-4">
          {[1, 2, 3, 4, 5].map((i) => (
            <div key={i} className="bg-zinc-900 border border-zinc-800 rounded-2xl p-4 flex items-center gap-4 group hover:bg-zinc-800/80 transition-colors">
              <button 
                onClick={() => setPlaying(playing === i ? null : i)}
                className={`w-12 h-12 flex-shrink-0 rounded-full flex items-center justify-center transition-colors ${
                  playing === i 
                    ? 'bg-yellow-500 text-black shadow-[0_0_15px_rgba(234,179,8,0.3)]' 
                    : 'bg-zinc-800 text-yellow-500 group-hover:bg-zinc-700'
                }`}
              >
                {playing === i ? <Pause size={20} className="fill-current" /> : <Play size={20} className="fill-current ml-1" />}
              </button>
              
              <div className="flex-1 min-w-0">
                <h3 className="font-bold text-white text-sm truncate mb-1">أهزوجة العشاق {i}</h3>
                <div className="flex items-center gap-3 text-xs text-zinc-400">
                  <span>أهازيج الكورفا</span>
                  <span>•</span>
                  <span>12K استماع</span>
                </div>
              </div>

              <button className="w-10 h-10 flex items-center justify-center rounded-full text-zinc-500 hover:text-red-500 hover:bg-red-500/10 transition-colors">
                <Heart size={20} />
              </button>
            </div>
          ))}
        </div>"""

ui_replace = """        <div className="space-y-4">
          {chants
            .filter(c => activeCategory === 'all' || c.category === activeCategory)
            .filter(c => c.title.includes(searchQuery) || c.lyrics.includes(searchQuery))
            .map(c => (
            <div key={c.id} className="bg-zinc-900 border border-zinc-800 rounded-2xl p-4 flex items-center gap-4 group hover:bg-zinc-800/80 transition-colors">
              <button 
                onClick={() => handlePlay(c)}
                className={`w-12 h-12 flex-shrink-0 rounded-full flex items-center justify-center transition-colors ${
                  playing === c.id 
                    ? 'bg-yellow-500 text-black shadow-[0_0_15px_rgba(234,179,8,0.3)]' 
                    : 'bg-zinc-800 text-yellow-500 group-hover:bg-zinc-700'
                }`}
              >
                {playing === c.id ? <Pause size={20} className="fill-current" /> : <Play size={20} className="fill-current ml-1" />}
              </button>
              
              <div className="flex-1 min-w-0">
                <h3 className="font-bold text-white text-sm truncate mb-1">{c.title}</h3>
                <div className="flex items-center gap-3 text-xs text-zinc-400">
                  <span>{c.category}</span>
                  <span>•</span>
                  <span>{c.views} استماع</span>
                </div>
              </div>

              <button className="w-10 h-10 flex items-center justify-center rounded-full text-zinc-500 hover:text-red-500 hover:bg-red-500/10 transition-colors">
                <Heart size={20} />
              </button>
            </div>
          ))}
          {chants.length === 0 && <p className="text-center text-zinc-500 text-sm">لا توجد أهازيج</p>}
        </div>"""
content = content.replace(ui_search, ui_replace)

with open("src/components/ChantsLibrary.tsx", "w") as f:
    f.write(content)

