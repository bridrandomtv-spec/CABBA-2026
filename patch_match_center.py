import sys

with open('src/components/MatchCenter.tsx', 'r') as f:
    content = f.read()

# Add import
content = content.replace("import InGameNotifications from './InGameNotifications';", "import InGameNotifications from './InGameNotifications';\nimport MatchHighlights from './MatchHighlights';")

# Add component to layout
content = content.replace("{activeTab === 'live' && (\n        <InGameNotifications />\n      )}", "{activeTab === 'live' && (\n        <>\n          <InGameNotifications />\n          <MatchHighlights />\n        </>\n      )}")

with open('src/components/MatchCenter.tsx', 'w') as f:
    f.write(content)
