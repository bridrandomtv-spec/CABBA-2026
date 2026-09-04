import re

with open("src/components/Home.tsx", "r") as f:
    content = f.read()

# Remove 'ساهم الآن مع الجراد الأصفر' button
content = re.sub(r"\s*<button onClick=\{\(\) => alert\('هذه الخاصية ستتوفر قريباً!'\)\}.*?>\s*ساهم الآن مع الجراد الأصفر\s*</button>", "", content, flags=re.DOTALL)

# Remove 'عرض الكل' buttons
content = re.sub(r"\s*<button onClick=\{\(\) => alert\('هذه الخاصية ستتوفر قريباً!'\)\}.*?>\s*عرض الكل\s*<ChevronLeft size=\{14\} />\s*</button>", "", content, flags=re.DOTALL)

with open("src/components/Home.tsx", "w") as f:
    f.write(content)
