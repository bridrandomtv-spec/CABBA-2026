import sys

with open('src/components/MatchCenter.tsx', 'r') as f:
    content = f.read()

if 'History' not in content:
    content = content.replace("import { Target } from 'lucide-react';", "import { Target, History } from 'lucide-react';")

with open('src/components/MatchCenter.tsx', 'w') as f:
    f.write(content)
