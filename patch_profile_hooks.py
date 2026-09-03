import re

with open("src/components/Profile.tsx", "r") as f:
    content = f.read()

# Remove the hooks from the middle
hooks_block = """  const { theme, toggleTheme } = useTheme();
  const { favorites } = useFavorites();
  const userName = localStorage.getItem('userName') || 'أمين. ب';
"""
content = content.replace(hooks_block, "")

# Insert them at the top of the function
target = "export default function Profile() {"
replacement = target + "\n" + hooks_block

content = content.replace(target, replacement)

with open("src/components/Profile.tsx", "w") as f:
    f.write(content)

