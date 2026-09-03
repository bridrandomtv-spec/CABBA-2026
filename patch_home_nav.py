import re

# Update App.tsx
with open("src/App.tsx", "r") as f:
    app_content = f.read()

app_content = app_content.replace("<Home />", "<Home onNavigate={setActiveTab} />")

with open("src/App.tsx", "w") as f:
    f.write(app_content)

# Update Home.tsx
with open("src/components/Home.tsx", "r") as f:
    home_content = f.read()

home_content = home_content.replace("export default function Home() {", """interface HomeProps {
  onNavigate?: (tab: any) => void;
}

export default function Home({ onNavigate }: HomeProps) {""")

old_button = """<button onClick={() => alert('هذه الخاصية ستتوفر قريباً!')} className="w-full bg-yellow-500 hover:bg-yellow-400 text-black text-sm font-bold py-3 px-4 rounded-xl flex items-center justify-center gap-2 transition-colors">
            مركز المباراة
            <ArrowLeft size={16} />
          </button>"""

new_button = """<button onClick={() => onNavigate && onNavigate('match')} className="w-full bg-yellow-500 hover:bg-yellow-400 text-black text-sm font-bold py-3 px-4 rounded-xl flex items-center justify-center gap-2 transition-colors">
            مركز المباراة
            <ArrowLeft size={16} />
          </button>"""

home_content = home_content.replace(old_button, new_button)

with open("src/components/Home.tsx", "w") as f:
    f.write(home_content)

