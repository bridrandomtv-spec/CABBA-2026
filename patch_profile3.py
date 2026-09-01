import sys

with open('src/components/Profile.tsx', 'r') as f:
    content = f.read()

content = content.replace("import FanChallenges from './FanChallenges';\n", "")
content = content.replace("<FanChallenges />\n      {/* Badges Section */}", "{/* Badges Section */}")

with open('src/components/Profile.tsx', 'w') as f:
    f.write(content)
