import re
import os

def process_file(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, "r") as f:
        content = f.read()

    # Generic button removal (rough regex to remove buttons that only alert "قريباً")
    # This might be tricky. Let's just do targeted replacements based on grep.

    # 1. Home.tsx
    if "Home.tsx" in filepath:
        content = re.sub(r'<button[^>]*alert\(\'هذه الخاصية ستتوفر قريباً!\'\)[^>]*>.*?</button>', '', content, flags=re.DOTALL)
    
    # 2. Profile.tsx
    if "Profile.tsx" in filepath:
        content = re.sub(r'<button[^>]*alert\(\'هذه الخاصية ستتوفر قريباً!\'\)[^>]*>.*?</button>', '', content, flags=re.DOTALL)
    
    # 3. Store.tsx
    if "Store.tsx" in filepath:
        content = re.sub(r'<button[^>]*alert\("سيتم توجيهك.*?"\)[^>]*>.*?</button>', '', content, flags=re.DOTALL)
        content = re.sub(r'<button[^>]*alert\("لا يمكن شراء التذاكر.*?"\)[^>]*>.*?</button>', '', content, flags=re.DOTALL)
        content = re.sub(r'<button[^>]*alert\("تمت إضافة المنتج إلى السلة بنجاح!"\)[^>]*>.*?</button>', '', content, flags=re.DOTALL)
        
    # 4. MatchCalendar.tsx
    if "MatchCalendar.tsx" in filepath:
        content = re.sub(r'<button[^>]*alert\(\'هذه الخاصية ستتوفر قريباً!\'\)[^>]*>.*?</button>', '', content, flags=re.DOTALL)

    # 5. MatchCenter.tsx
    if "MatchCenter.tsx" in filepath:
        content = re.sub(r'<button[^>]*alert\(\'هذه الخاصية ستتوفر قريباً!\'\)[^>]*>.*?</button>', '', content, flags=re.DOTALL)
        
    # 6. FanCommunity.tsx
    if "FanCommunity.tsx" in filepath:
        # Instead of removing, maybe change to silent or keep alert.
        pass

    with open(filepath, "w") as f:
        f.write(content)

files = [
    "src/components/Home.tsx",
    "src/components/Profile.tsx",
    "src/components/Store.tsx",
    "src/components/MatchCalendar.tsx",
    "src/components/MatchCenter.tsx",
    "src/components/FanCommunity.tsx"
]

for file in files:
    process_file(file)

