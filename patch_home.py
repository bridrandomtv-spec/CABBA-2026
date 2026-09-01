import sys

with open('src/components/Home.tsx', 'r') as f:
    content = f.read()

content = content.replace("import ClubHistory from './ClubHistory';", "import ClubHistory from './ClubHistory';\nimport WeatherWidget from './WeatherWidget';")

old_section = """      <TeamStats />

      {/* History Navigation Card */}"""

new_section = """      <TeamStats />
      
      <WeatherWidget />

      {/* History Navigation Card */}"""

content = content.replace(old_section, new_section)

with open('src/components/Home.tsx', 'w') as f:
    f.write(content)
