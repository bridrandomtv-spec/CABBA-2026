import sys

with open('src/components/FanGallery.tsx', 'r') as f:
    content = f.read()

content = content.replace("'/src/assets/images/fan_selfie_stadium_1785338098289.jpg'", "'https://images.unsplash.com/photo-1614632537190-23e4146777db?auto=format&fit=crop&q=80&w=400&h=400'")
content = content.replace("'/src/assets/images/fans_cheering_1785338114820.jpg'", "'https://images.unsplash.com/photo-1522778119026-d647f0596c20?auto=format&fit=crop&q=80&w=400&h=400'")

with open('src/components/FanGallery.tsx', 'w') as f:
    f.write(content)

with open('src/components/ClubHistory.tsx', 'r') as f:
    content2 = f.read()

content2 = content2.replace("'/src/assets/images/cabba_history_1931_1785337677767.jpg'", "'https://images.unsplash.com/photo-1518605368461-1e1e38ce7058?auto=format&fit=crop&q=80&w=800'")
content2 = content2.replace("'/src/assets/images/cabba_victory_1998_1785337711795.jpg'", "'https://images.unsplash.com/photo-1579952363873-27f3bade9f55?auto=format&fit=crop&q=80&w=800'")
content2 = content2.replace("'/src/assets/images/cabba_stadium_1990_1785337695008.jpg'", "'https://images.unsplash.com/photo-1459865264687-595d652de67e?auto=format&fit=crop&q=80&w=800'")

with open('src/components/ClubHistory.tsx', 'w') as f:
    f.write(content2)
