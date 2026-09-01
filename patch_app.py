import sys

with open('src/App.tsx', 'r') as f:
    content = f.read()

content = content.replace("import MatchAlert from './components/MatchAlert';", "import MatchAlert from './components/MatchAlert';\nimport NotificationCenter from './components/NotificationCenter';")
content = content.replace("const [showOnboarding, setShowOnboarding] = useState(false);", "const [showOnboarding, setShowOnboarding] = useState(false);\n  const [showNotifications, setShowNotifications] = useState(false);")

old_header = """          <div className="w-8 h-8 rounded-full bg-zinc-800 flex items-center justify-center relative border border-zinc-700">
            <div className="w-2 h-2 rounded-full bg-red-500 absolute top-1 right-1"></div>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="text-zinc-400"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/></svg>
          </div>"""

new_header = """          <button 
            onClick={() => setShowNotifications(true)}
            className="w-8 h-8 rounded-full bg-zinc-800 flex items-center justify-center relative border border-zinc-700 hover:bg-zinc-700 transition-colors"
          >
            <div className="w-2 h-2 rounded-full bg-red-500 absolute top-1 right-1"></div>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="text-zinc-400"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/></svg>
          </button>"""

content = content.replace(old_header, new_header)

old_bottom = """        {showOnboarding && <OnboardingCarousel onComplete={handleOnboardingComplete} />}"""

new_bottom = """        {showOnboarding && <OnboardingCarousel onComplete={handleOnboardingComplete} />}
        {showNotifications && <NotificationCenter onClose={() => setShowNotifications(false)} />}"""

content = content.replace(old_bottom, new_bottom)

with open('src/App.tsx', 'w') as f:
    f.write(content)
