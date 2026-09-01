import sys

with open('src/components/Home.tsx', 'r') as f:
    content = f.read()

content = content.replace("import WeatherWidget from './WeatherWidget';", "import WeatherWidget from './WeatherWidget';\nimport FanPolls from './FanPolls';")

old_section = """      <WeatherWidget />

      {/* History Navigation Card */}"""

new_section = """      <WeatherWidget />
      
      <FanPolls />

      {/* History Navigation Card */}"""

content = content.replace(old_section, new_section)

with open('src/components/Home.tsx', 'w') as f:
    f.write(content)
