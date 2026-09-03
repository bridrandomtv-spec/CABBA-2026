import re

with open("src/components/Store.tsx", "r") as f:
    content = f.read()

content = content.replace(
    '<button className="bg-black text-yellow-500 text-xs font-bold py-2 px-4 rounded-lg relative z-10 hover:bg-zinc-900 transition-colors">',
    '<button onClick={() => alert("سيتم توجيهك إلى صفحة تخصيص القميص (قريباً)")} className="bg-black text-yellow-500 text-xs font-bold py-2 px-4 rounded-lg relative z-10 hover:bg-zinc-900 transition-colors">'
)

content = content.replace(
    '<button className="w-8 h-8 rounded-full bg-zinc-800 flex items-center justify-center text-white hover:bg-yellow-500 hover:text-black transition-colors">',
    '<button onClick={() => alert("تمت إضافة المنتج إلى السلة بنجاح!")} className="w-8 h-8 rounded-full bg-zinc-800 flex items-center justify-center text-white hover:bg-yellow-500 hover:text-black transition-colors">'
)

content = content.replace(
    '<button className="bg-zinc-800 text-white text-sm font-bold py-2 px-6 rounded-lg opacity-50 cursor-not-allowed">',
    '<button onClick={() => alert("لا يمكن شراء التذاكر حالياً. سيتم فتح البيع قريباً.")} className="bg-zinc-800 text-white text-sm font-bold py-2 px-6 rounded-lg opacity-50 cursor-not-allowed">'
)

with open("src/components/Store.tsx", "w") as f:
    f.write(content)

