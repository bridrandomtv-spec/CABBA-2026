import sys
with open('src/components/MatchMVP.tsx', 'r') as f:
    content = f.read()

old_percent = "const percentage = totalVotes > 0 ? Math.round((candidate.votes / (totalVotes + (votedCandidate ? 1 : 0))) * 100) : 0;"
new_percent = "const percentage = totalVotes > 0 ? Math.round((candidate.votes / totalVotes) * 100) : 0;"
content = content.replace(old_percent, new_percent)

with open('src/components/MatchMVP.tsx', 'w') as f:
    f.write(content)
