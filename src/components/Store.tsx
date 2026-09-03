import { useState } from 'react';
import { ShoppingCart, QrCode, Tag, ExternalLink } from 'lucide-react';
import { Product } from '../types';

export default function Store() {
  const [activeTab, setActiveTab] = useState<'merch' | 'tickets'>('merch');

  const products: Product[] = [
    { id: '1', name: 'القميص الأساسي 2026', price: 4500, category: 'kit', imageUrl: 'C' },
    { id: '2', name: 'وشاح الجراد الأصفر', price: 1200, category: 'merch', imageUrl: 'C' },
    { id: '3', name: 'القميص الاحتياطي', price: 4500, category: 'kit', imageUrl: 'C' },
    { id: '4', name: 'قبعة الكابا', price: 800, category: 'merch', imageUrl: 'C' },
  ];

  return (
    <div className="p-4 space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-500" dir="rtl">
      {/* Header Tabs */}
      <div className="flex p-1 bg-zinc-900 rounded-xl border border-zinc-800 shadow-sm">
        <button
          onClick={() => setActiveTab('merch')}
          className={`flex-1 py-2 text-sm font-bold rounded-lg flex items-center justify-center gap-2 transition-all ${
            activeTab === 'merch' ? 'bg-zinc-800 text-yellow-500 shadow-sm' : 'text-zinc-500 hover:text-zinc-300'
          }`}
        >
          <ShoppingCart size={16} />
          المتجر
        </button>
        <button
          onClick={() => setActiveTab('tickets')}
          className={`flex-1 py-2 text-sm font-bold rounded-lg flex items-center justify-center gap-2 transition-all ${
            activeTab === 'tickets' ? 'bg-zinc-800 text-yellow-500 shadow-sm' : 'text-zinc-500 hover:text-zinc-300'
          }`}
        >
          <QrCode size={16} />
          التذاكر الرقمية
        </button>
      </div>

      {activeTab === 'merch' ? (
        <div className="space-y-4">
          <div className="bg-gradient-to-l from-yellow-500 to-yellow-600 rounded-2xl p-5 text-black relative overflow-hidden shadow-lg">
            <div className="absolute left-0 top-0 w-32 h-32 bg-white/20 rounded-full blur-2xl -translate-x-10 -translate-y-10"></div>
            <h3 className="font-bold text-lg mb-1 relative z-10">جديد المتجر</h3>
            <p className="text-sm font-medium mb-4 relative z-10 opacity-80">احصل على القميص الرسمي الآن مع تخصيص الاسم والرقم</p>
            <button onClick={() => alert("سيتم توجيهك إلى صفحة تخصيص القميص (قريباً)")} className="bg-black text-yellow-500 text-xs font-bold py-2 px-4 rounded-lg relative z-10 hover:bg-zinc-900 transition-colors">
              اطلب الآن
            </button>
          </div>

          <div className="grid grid-cols-2 gap-3">
            {products.map((product) => (
              <div key={product.id} className="bg-zinc-900 border border-zinc-800 rounded-xl p-3 flex flex-col group hover:border-yellow-500/50 transition-all">
                <div className="aspect-square bg-zinc-800 rounded-lg mb-3 flex items-center justify-center relative overflow-hidden">
                  <div className="text-yellow-500/20 text-5xl font-black group-hover:scale-110 transition-transform">
                    {product.imageUrl}
                  </div>
                  {product.category === 'kit' && (
                    <span className="absolute top-2 right-2 bg-yellow-500 text-black text-[9px] font-bold px-1.5 py-0.5 rounded">
                      رسمي
                    </span>
                  )}
                </div>
                <h4 className="font-bold text-sm text-white mb-1 line-clamp-1">{product.name}</h4>
                <div className="flex justify-between items-end mt-auto pt-2">
                  <span className="text-yellow-500 font-bold text-sm">{product.price} د.ج</span>
                  <button onClick={() => alert("تمت إضافة المنتج إلى السلة بنجاح!")} className="w-8 h-8 rounded-full bg-zinc-800 flex items-center justify-center text-white hover:bg-yellow-500 hover:text-black transition-colors">
                    <ShoppingCart size={14} />
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      ) : (
        <div className="space-y-4">
          <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-5 flex items-center gap-4">
            <div className="w-12 h-12 rounded-full bg-zinc-800 flex items-center justify-center text-yellow-500 shrink-0">
              <QrCode size={24} />
            </div>
            <div>
              <h3 className="font-bold text-white mb-1">بطاقة العبور الرقمية</h3>
              <p className="text-xs text-zinc-400">استخدم التطبيق لدخول الملعب مباشرة لتفادي الطوابير والسوق السوداء.</p>
            </div>
          </div>

          <div className="bg-zinc-900 border-2 border-dashed border-zinc-700 rounded-2xl p-6 text-center mt-6">
            <Tag size={40} className="text-zinc-600 mx-auto mb-4" />
            <h4 className="font-bold text-white mb-2">لا توجد تذاكر متاحة حالياً</h4>
            <p className="text-sm text-zinc-400 mb-6">سيتم فتح عملية البيع للمباراة القادمة قبل 48 ساعة من موعد الانطلاق.</p>
            <button onClick={() => alert("لا يمكن شراء التذاكر حالياً. سيتم فتح البيع قريباً.")} className="bg-zinc-800 text-white text-sm font-bold py-2 px-6 rounded-lg ">
              شراء تذكرة
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
