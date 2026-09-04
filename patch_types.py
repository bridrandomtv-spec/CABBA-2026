import re

with open("src/types.ts", "r") as f:
    content = f.read()

# Update the Tab type
tab_search = "export type Tab = 'home' | 'match' | 'chants' | 'tv' | 'store' | 'profile' | 'community';"
tab_replace = "export type Tab = 'home' | 'match' | 'chants' | 'tv' | 'store' | 'profile' | 'community' | 'admin';"
content = content.replace(tab_search, tab_replace)

with open("src/types.ts", "w") as f:
    f.write(content)

