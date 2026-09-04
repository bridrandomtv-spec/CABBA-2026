import re

with open("src/components/Store.tsx", "r") as f:
    content = f.read()

import_search = "import { ShoppingCart, Search, Filter, Plus, Minus, X, CreditCard } from 'lucide-react';"
import_replace = "import { ShoppingCart, Search, Filter, Plus, Minus, X, CreditCard } from 'lucide-react';\nimport { useState, useEffect } from 'react';\nimport { collection, query, orderBy, onSnapshot, addDoc } from 'firebase/firestore';\nimport { db } from '../lib/firebase';\nimport { Product } from './admin/AdminStore';\nimport { useAuth } from '../contexts/AuthContext';"
content = content.replace(import_search, import_replace)

body_search = """export default function Store() {
  const [activeCategory, setActiveCategory] = useState('all');
  const [showCart, setShowCart] = useState(false);
  const [cart, setCart] = useState<any[]>([]);"""
  
body_replace = """export default function Store() {
  const { currentUser } = useAuth();
  const [products, setProducts] = useState<Product[]>([]);
  const [activeCategory, setActiveCategory] = useState('all');
  const [showCart, setShowCart] = useState(false);
  const [cart, setCart] = useState<any[]>([]);
  const [loadingCheckout, setLoadingCheckout] = useState(false);

  useEffect(() => {
    const q = query(collection(db, 'products'), orderBy('createdAt', 'desc'));
    const un = onSnapshot(q, (snapshot) => {
      const data: Product[] = [];
      snapshot.forEach(doc => {
        const p = { id: doc.id, ...doc.data() } as Product;
        if (p.active) data.push(p);
      });
      setProducts(data);
    });
    return () => un();
  }, []);
"""
content = content.replace(body_search, body_replace)

cart_logic_search = """  const checkout = () => {
    alert('تم تأكيد الطلب بنجاح! سيتم التواصل معك قريباً');
    setCart([]);
    setShowCart(false);
  };"""

cart_logic_replace = """  const checkout = async () => {
    if (!currentUser) {
      alert('يجب تسجيل الدخول لإتمام الطلب');
      return;
    }
    setLoadingCheckout(true);
    try {
      await addDoc(collection(db, 'orders'), {
        userId: currentUser.uid,
        items: cart,
        total: cartTotal,
        status: 'pending',
        createdAt: Date.now()
      });
      alert('تم تأكيد الطلب بنجاح! سيتم التواصل معك قريباً');
      setCart([]);
      setShowCart(false);
    } catch (e) {
      console.error(e);
      alert('حدث خطأ أثناء إتمام الطلب');
    } finally {
      setLoadingCheckout(false);
    }
  };"""
content = content.replace(cart_logic_search, cart_logic_replace)

ui_search = """        <div className="grid grid-cols-2 gap-4">
          {[1, 2, 3, 4, 5, 6].map((i) => (
            <div key={i} className="bg-zinc-900 border border-zinc-800 rounded-2xl overflow-hidden group">
              <div className="relative h-40 bg-zinc-800 p-4">
                <img 
                  src={`https://images.unsplash.com/photo-1577223625816-7546f13df25d?w=400&h=400&fit=crop&q=80&${i}`}
                  alt="Product"
                  className="w-full h-full object-contain group-hover:scale-110 transition-transform duration-300"
                />
                {i === 1 && (
                  <div className="absolute top-2 right-2 bg-yellow-500 text-black text-[10px] font-bold px-2 py-1 rounded-md">
                    جديد
                  </div>
                )}
              </div>
              <div className="p-3">
                <h3 className="font-bold text-white text-sm mb-1 truncate">قميص أهلي البرج الرسمي 2026</h3>
                <p className="text-yellow-500 font-bold text-sm mb-3">4,500 دج</p>
                <button 
                  onClick={() => addToCart({ id: i, name: `قميص الفريق ${i}`, price: 4500, image: `https://images.unsplash.com/photo-1577223625816-7546f13df25d?w=400&h=400&fit=crop&q=80&${i}` })}
                  className="w-full bg-zinc-800 hover:bg-yellow-500 text-zinc-300 hover:text-black text-xs font-bold py-2 rounded-xl transition-colors flex items-center justify-center gap-2"
                >
                  <ShoppingCart size={14} />
                  أضف للسلة
                </button>
              </div>
            </div>
          ))}
        </div>"""

ui_replace = """        <div className="grid grid-cols-2 gap-4">
          {products.filter(p => activeCategory === 'all' || p.category === activeCategory).map((p) => (
            <div key={p.id} className="bg-zinc-900 border border-zinc-800 rounded-2xl overflow-hidden group">
              <div className="relative h-40 bg-zinc-800 p-2">
                <img 
                  src={p.image}
                  alt={p.name}
                  className="w-full h-full object-cover rounded-xl group-hover:scale-105 transition-transform duration-300"
                />
                {p.stock <= 5 && p.stock > 0 && (
                  <div className="absolute top-2 right-2 bg-red-500 text-white text-[10px] font-bold px-2 py-1 rounded-md">
                    كمية محدودة
                  </div>
                )}
                {p.stock === 0 && (
                  <div className="absolute inset-0 bg-black/60 flex items-center justify-center">
                    <span className="bg-red-500 text-white text-xs font-bold px-2 py-1 rounded">نفدت الكمية</span>
                  </div>
                )}
              </div>
              <div className="p-3">
                <h3 className="font-bold text-white text-sm mb-1 truncate">{p.name}</h3>
                <p className="text-yellow-500 font-bold text-sm mb-3">{p.price} دج</p>
                <button 
                  disabled={p.stock === 0}
                  onClick={() => addToCart({ id: p.id, name: p.name, price: p.price, image: p.image })}
                  className="w-full bg-zinc-800 hover:bg-yellow-500 text-zinc-300 hover:text-black text-xs font-bold py-2 rounded-xl transition-colors flex items-center justify-center gap-2 disabled:opacity-50 disabled:hover:bg-zinc-800 disabled:hover:text-zinc-300"
                >
                  <ShoppingCart size={14} />
                  {p.stock === 0 ? 'نفدت الكمية' : 'أضف للسلة'}
                </button>
              </div>
            </div>
          ))}
          {products.length === 0 && <p className="text-center text-zinc-500 text-sm col-span-2">لا توجد منتجات حالياً</p>}
        </div>"""
content = content.replace(ui_search, ui_replace)

checkout_btn_search = """              <button 
                onClick={checkout}
                className="w-full bg-yellow-500 hover:bg-yellow-400 text-black font-bold py-3 rounded-xl transition-colors flex items-center justify-center gap-2"
              >
                <CreditCard size={18} />
                تأكيد الطلب
              </button>"""

checkout_btn_replace = """              <button 
                onClick={checkout}
                disabled={loadingCheckout}
                className="w-full bg-yellow-500 hover:bg-yellow-400 text-black font-bold py-3 rounded-xl transition-colors flex items-center justify-center gap-2 disabled:opacity-50"
              >
                <CreditCard size={18} />
                {loadingCheckout ? 'جاري المعالجة...' : 'تأكيد الطلب'}
              </button>"""
content = content.replace(checkout_btn_search, checkout_btn_replace)

with open("src/components/Store.tsx", "w") as f:
    f.write(content)

