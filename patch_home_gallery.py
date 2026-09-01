import sys

with open('src/components/Home.tsx', 'r') as f:
    content = f.read()

content = content.replace("import FanPolls from './FanPolls';", "import FanPolls from './FanPolls';\nimport FanGallery from './FanGallery';")

old_section = """      <FanPolls />

      {/* History Navigation Card */}"""

new_section = """      <FanPolls />
      
      <FanGallery />

      {/* History Navigation Card */}"""

content = content.replace(old_section, new_section)

with open('src/components/Home.tsx', 'w') as f:
    f.write(content)
