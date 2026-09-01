import sys

with open('src/components/MatchMVP.tsx', 'r') as f:
    content = f.read()

# Add Share2 icon import
content = content.replace("import { Star, CheckCircle2 } from 'lucide-react';", "import { Star, CheckCircle2, Share2 } from 'lucide-react';")

# Add handleShare function
old_handleVote = """  const handleVote = (candidateId: string) => {
    if (votedCandidate) return;
    setVotedCandidate(candidateId);
    setCandidates(prev => 
      prev.map(c => 
        c.id === candidateId ? { ...c, votes: c.votes + 1 } : c
      ).sort((a, b) => b.votes - a.votes)
    );
  };"""

new_handleVote = """  const handleVote = (candidateId: string) => {
    if (votedCandidate) return;
    setVotedCandidate(candidateId);
    setCandidates(prev => 
      prev.map(c => 
        c.id === candidateId ? { ...c, votes: c.votes + 1 } : c
      ).sort((a, b) => b.votes - a.votes)
    );
  };

  const handleShare = async () => {
    const votedFor = candidates.find(c => c.id === votedCandidate);
    if (!votedFor) return;
    
    const shareData = {
      title: 'نجم المباراة',
      text: `لقد صوّتت للاعب ${votedFor.name} كأفضل لاعب في المباراة! صوت الآن عبر تطبيق الجراد الأصفر.`,
      url: window.location.href,
    };

    try {
      if (navigator.share) {
        await navigator.share(shareData);
      } else {
        // Fallback
        const xUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(shareData.text)}&url=${encodeURIComponent(shareData.url)}`;
        window.open(xUrl, '_blank');
      }
    } catch (err) {
      console.log('Error sharing:', err);
    }
  };"""

content = content.replace(old_handleVote, new_handleVote)

# Add share button to voted state message
old_voted_msg = """      {votedCandidate && (
        <div className="mt-6 text-center text-xs text-yellow-500 bg-yellow-500/10 border border-yellow-500/20 py-2 rounded-lg font-bold">
          تم تسجيل تصويتك بنجاح! شكراً لمشاركتك.
        </div>
      )}"""

new_voted_msg = """      {votedCandidate && (
        <div className="mt-6 flex flex-col gap-3">
          <div className="text-center text-xs text-yellow-500 bg-yellow-500/10 border border-yellow-500/20 py-2 rounded-lg font-bold">
            تم تسجيل تصويتك بنجاح! شكراً لمشاركتك.
          </div>
          <button 
            onClick={handleShare}
            className="w-full bg-zinc-800 hover:bg-zinc-700 border border-zinc-700 text-white text-sm font-bold py-2.5 rounded-xl transition-colors flex items-center justify-center gap-2"
          >
            <Share2 size={16} /> شارك تصويتك
          </button>
        </div>
      )}"""

content = content.replace(old_voted_msg, new_voted_msg)

with open('src/components/MatchMVP.tsx', 'w') as f:
    f.write(content)

