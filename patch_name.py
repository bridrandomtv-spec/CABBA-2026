import re

with open("src/components/Profile.tsx", "r") as f:
    content = f.read()

# Replace hardcoded name with a state variable that reads from localStorage
# Find this pattern: <p className="text-white font-bold text-lg">أمين. ب</p>
if 'const userName = localStorage.getItem("userName") || "أمين. ب";' not in content:
    # insert userName constant right after `const { favorites } = useFavorites();`
    content = content.replace("const { favorites } = useFavorites();", "const { favorites } = useFavorites();\n  const userName = localStorage.getItem('userName') || 'أمين. ب';")

# replace hardcoded UI name
content = content.replace('<p className="text-white font-bold text-lg">أمين. ب</p>', '<p className="text-white font-bold text-lg">{userName}</p>')

# Also replace the initial letter placeholder if needed
content = content.replace('alt="صورة المناصر"', f'alt={{`صورة ${"{userName}"}`}}')

with open("src/components/Profile.tsx", "w") as f:
    f.write(content)
