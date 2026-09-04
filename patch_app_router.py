import re

with open("src/App.tsx", "r") as f:
    content = f.read()

state_search = "  const [activeTab, setActiveTab] = useState<Tab>('home');"
state_replace = """  const [activeTab, setActiveTab] = useState<Tab>(() => {
    return (sessionStorage.getItem('activeTab') as Tab) || 'home';
  });

  useEffect(() => {
    sessionStorage.setItem('activeTab', activeTab);
  }, [activeTab]);"""
content = content.replace(state_search, state_replace)

with open("src/App.tsx", "w") as f:
    f.write(content)

