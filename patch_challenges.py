import re

with open("src/components/FanChallenges.tsx", "r") as f:
    content = f.read()

# Add a function to complete the challenge
complete_logic = """  const handleClaim = (id: number) => {
    setClaimed(prev => ({ ...prev, [id]: true }));
    // In a real app, this would update the user's total points and badges
  };

  const handleAction = (id: number) => {
    if (id === 1) {
      alert("سيتم فتح الكاميرا قريباً لالتقاط صورتك!");
    } else if (id === 2) {
      alert("تم تسجيل المقطع الصوتي بنجاح! لقد أكملت التحدي.");
    }
    
    // Mark as completed
    setChallenges(prev => prev.map(c => 
      c.id === id ? { ...c, completed: true } : c
    ));
  };
"""

content = content.replace("""  const handleClaim = (id: number) => {
    setClaimed(prev => ({ ...prev, [id]: true }));
    // In a real app, this would update the user's total points and badges
  };""", complete_logic)


# Update the button
old_button = """              {!challenge.completed && challenge.actionText && (
                <button onClick={() => alert('هذه الخاصية ستتوفر قريباً!')} className="mt-4 w-full bg-zinc-800 hover:bg-zinc-700 text-white text-xs font-bold py-2 rounded-lg transition-colors border border-zinc-700">
                  {challenge.actionText}
                </button>
              )}"""

new_button = """              {!challenge.completed && challenge.actionText && (
                <button onClick={() => handleAction(challenge.id)} className="mt-4 w-full bg-zinc-800 hover:bg-zinc-700 text-white text-xs font-bold py-2 rounded-lg transition-colors border border-zinc-700 group hover:border-yellow-500/50">
                  <span className="group-hover:text-yellow-500 transition-colors">{challenge.actionText}</span>
                </button>
              )}"""

content = content.replace(old_button, new_button)

with open("src/components/FanChallenges.tsx", "w") as f:
    f.write(content)

