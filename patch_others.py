import re

with open("src/components/MatchPredictions.tsx", "r") as f:
    content = f.read()

content = re.sub(r"\s*<button onClick=\{\(\) => alert\('هذه الخاصية ستتوفر قريباً!'\)\}.*?>\s*هذا الأسبوع <ChevronDown.*?>\s*</button>", "", content, flags=re.DOTALL)

with open("src/components/MatchPredictions.tsx", "w") as f:
    f.write(content)

with open("src/components/FanGallery.tsx", "r") as f:
    content = f.read()

content = re.sub(r"\s*<button onClick=\{\(\) => alert\('هذه الخاصية ستتوفر قريباً!'\)\}.*?>\s*شارك صورتك\s*</button>", "", content, flags=re.DOTALL)
content = re.sub(r"\s*<button onClick=\{\(\) => alert\('هذه الخاصية ستتوفر قريباً!'\)\}.*?>\s*<MessageCircle.*?>\s*<span>\{post.comments\}</span>\s*</button>", "", content, flags=re.DOTALL)

with open("src/components/FanGallery.tsx", "w") as f:
    f.write(content)
