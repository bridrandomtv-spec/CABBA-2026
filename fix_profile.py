import re

with open("src/components/Profile.tsx", "r") as f:
    content = f.read()

# Remove duplicate `const { logout } = useAuth();`
# Auth is destructured from `const { currentUser, userData, logout } = useAuth();` already at the top of Profile
content = content.replace("  const handleLogout = async () => {\n    const { logout } = useAuth();", "  const handleLogout = async () => {")

# Remove any remaining setIsLoggedIn
content = re.sub(r"setIsLoggedIn\(.*?\);", "", content)

# Check if handleLogout has a duplicated logout definition inside it
content = content.replace("    const { logout } = useAuth();\n", "")

with open("src/components/Profile.tsx", "w") as f:
    f.write(content)
