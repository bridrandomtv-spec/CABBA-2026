import re

with open("src/components/FanCommunity.tsx", "r") as f:
    content = f.read()

content = content.replace("          </div>\n}", "          </div>")

with open("src/components/FanCommunity.tsx", "w") as f:
    f.write(content)
