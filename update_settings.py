import sys

with open('src/components/NotificationSettings.tsx', 'r') as f:
    content = f.read()

# Replace useState initialization
old_init = """  const [settings, setSettings] = useState({
    goals: true,
    breakingNews: true,
    matches: false,
  });"""
new_init = """  const [settings, setSettings] = useState(() => {
    const saved = localStorage.getItem('cabba-notifications');
    if (saved) return JSON.parse(saved);
    return {
      goals: true,
      breakingNews: true,
      matches: false,
    };
  });"""

content = content.replace(old_init, new_init)

# Replace toggleSetting
old_toggle = """  const toggleSetting = (key: keyof typeof settings) => {
    setSettings(prev => ({ ...prev, [key]: !prev[key] }));
  };"""
new_toggle = """  const toggleSetting = (key: keyof typeof settings) => {
    setSettings((prev: any) => {
      const newSettings = { ...prev, [key]: !prev[key] };
      localStorage.setItem('cabba-notifications', JSON.stringify(newSettings));
      
      // Dispatch custom event so App.tsx can react to changes
      window.dispatchEvent(new Event('cabba-notifications-updated'));
      
      return newSettings;
    });
  };"""

content = content.replace(old_toggle, new_toggle)

with open('src/components/NotificationSettings.tsx', 'w') as f:
    f.write(content)
