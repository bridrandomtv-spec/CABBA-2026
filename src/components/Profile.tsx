import { Award, Shield, Settings, CheckCircle2, ChevronLeft, Moon, Sun, Heart, Calendar as CalendarIcon, MapPin } from 'lucide-react';
import { useFavorites } from '../hooks/useFavorites';
import { MATCHES_DATA } from './MatchCalendar';
import NotificationSettings from './NotificationSettings';
import Achievements from './Achievements';
import { QRCodeSVG } from 'qrcode.react';
import { useTheme } from '../ThemeContext';

export default function Profile() {
  const { theme, toggleTheme } = useTheme();
  const { favorites } = useFavorites();
  const favoriteMatches = MATCHES_DATA.filter(m => favorites.includes(m.id));

  return (
    <div className="p-4 space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-500" dir="rtl">
      
      {/* Digital Membership Card */}
      <div className="relative rounded-2xl overflow-hidden bg-gradient-to-tr from-black via-zinc-900 to-black border border-yellow-500/30 p-6 shadow-[0_10px_30px_rgba(234,179,8,0.1)]">
        <div className="absolute top-0 right-0 w-64 h-64 bg-yellow-500/10 rounded-full blur-3xl -translate-y-1/2 translate-x-1/3"></div>
        
        <div className="relative z-10 flex justify-between items-start mb-8">
          <div>
            <h2 className="text-yellow-500 font-bold tracking-widest text-sm mb-1 uppercase">عضوية شرفية</h2>
            <div className="text-white text-2xl font-black font-mono">CABBA-8291-04</div>
          </div>
          <div className="w-12 h-12 bg-yellow-500 rounded-full flex items-center justify-center border-2 border-black">
            <span className="font-bold text-black text-xl">C</span>
          </div>
        </div>
        
        <div className="relative z-10 flex justify-between items-end">
          <div className="flex items-center gap-3">
            <div className="w-12 h-12 rounded-lg bg-zinc-800 border-2 border-yellow-500 overflow-hidden shadow-lg">
              <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Amine&backgroundColor=f59e0b" alt="صورة المناصر" className="w-full h-full object-cover" />
            </div>
            <div>
              <p className="text-zinc-500 text-xs mb-1 uppercase tracking-wider">الاسم واللقب</p>
              <p className="text-white font-bold text-lg">أمين. ب</p>
            </div>
          </div>
          
          <div className="p-2 rounded-xl" style={{ backgroundColor: "#ffffff" }}>
            <QRCodeSVG value="CABBA-FAN-847291" size={48} />
          </div>
        </div>
      </div>

      {/* Digital Tickets */}
      <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-5 shadow-sm">
        <div className="flex items-center justify-between mb-4">
          <h3 className="font-bold text-white text-lg">التذاكر الرقمية</h3>
          <span className="text-xs text-green-500 font-bold bg-green-500/10 px-2 py-1 rounded-md border border-green-500/20">تذكرة واحدة نشطة</span>
        </div>
        
        <div className="bg-zinc-800/50 rounded-xl p-4 border border-zinc-700/50 flex flex-col items-center">
          <div className="flex justify-between items-center w-full mb-4">
            <div className="flex items-center gap-2">
              <span className="font-bold text-white text-sm">الكابا</span>
            </div>
            <span className="text-zinc-500 text-xs font-bold px-2">ضد</span>
            <div className="flex items-center gap-2">
              <span className="font-bold text-white text-sm">المنافس</span>
            </div>
          </div>
          
          <div className="p-3 rounded-xl mb-4 shadow-[0_0_15px_rgba(255,255,255,0.1)]" style={{ backgroundColor: "#ffffff" }}>
            <QRCodeSVG value="TICKET-78X92" size={96} />
          </div>
          
          <div className="flex flex-col items-center gap-1">
            <span className="text-xs text-zinc-400">ملعب 20 أوت 1955</span>
            <span className="font-bold text-yellow-500 text-sm tracking-widest">TICKET-78X92</span>
          </div>
        </div>
      </div>

      {/* Favorite Matches */}
      <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-5 shadow-sm">
        <div className="flex items-center justify-between mb-4">
          <h3 className="font-bold text-white text-lg flex items-center gap-2">
            <Heart className="text-red-500 fill-current" size={20} />
            المباريات المفضلة
          </h3>
          <span className="text-xs text-zinc-500 font-bold bg-zinc-800 px-2 py-1 rounded-md">{favorites.length} مباريات</span>
        </div>
        
        <div className="space-y-3">
          {favoriteMatches.length > 0 ? (
            favoriteMatches.map(match => (
              <div key={match.id} className="bg-zinc-800/50 border border-zinc-700/50 rounded-xl p-3 flex justify-between items-center">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 bg-zinc-800 rounded-full flex items-center justify-center border-2 border-zinc-700">
                    <span className="font-bold text-xs text-white truncate max-w-[20px]">{match.opponent.charAt(0)}</span>
                  </div>
                  <div>
                    <h4 className="font-bold text-white text-sm">{match.opponent}</h4>
                    <div className="flex items-center gap-1 text-[10px] text-zinc-500 mt-0.5">
                      <CalendarIcon size={10} /> {match.date}
                    </div>
                  </div>
                </div>
                <div className="flex flex-col items-center">
                  {match.status === 'past' ? (
                    <span className="font-bold text-white tracking-widest">{match.score}</span>
                  ) : (
                    <span className="text-xs font-bold text-yellow-500">{match.time}</span>
                  )}
                </div>
              </div>
            ))
          ) : (
            <div className="text-center py-6">
              <Heart size={32} className="text-zinc-700 mx-auto mb-2" />
              <p className="text-xs text-zinc-500">لم تقم بإضافة أي مباراة للمفضلة بعد.</p>
            </div>
          )}
        </div>
      </div>

      {/* Gamification / Loyalty Points */}
      <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-5 shadow-sm">
        <div className="flex justify-between items-center mb-6">
          <div className="flex items-center gap-3">
            <div className="bg-yellow-500/20 p-2 rounded-xl">
              <Award className="text-yellow-500" size={24} />
            </div>
            <div>
              <h3 className="font-bold text-white text-lg">1,450 نقطة</h3>
              <p className="text-xs text-zinc-400">نقاط الولاء (الجراد الأصفر)</p>
            </div>
          </div>
          <div className="text-left">
            <span className="bg-zinc-800 text-white text-xs font-bold px-3 py-1 rounded-full">المستوى 4</span>
          </div>
        </div>

        <div className="space-y-3">
          <button className="w-full bg-zinc-800 hover:bg-zinc-700 transition-colors p-3 rounded-xl flex items-center justify-between group">
            <div className="flex items-center gap-3">
              <Shield size={18} className="text-zinc-400 group-hover:text-yellow-500 transition-colors" />
              <span className="text-sm text-white font-medium">توقع مباريات الكابا</span>
            </div>
            <ChevronLeft size={16} className="text-zinc-500" />
          </button>
          
          <button className="w-full bg-zinc-800 hover:bg-zinc-700 transition-colors p-3 rounded-xl flex items-center justify-between group">
            <div className="flex items-center gap-3">
              <CheckCircle2 size={18} className="text-zinc-400 group-hover:text-yellow-500 transition-colors" />
              <span className="text-sm text-white font-medium">استبدال النقاط بالمكافآت</span>
            </div>
            <ChevronLeft size={16} className="text-zinc-500" />
          </button>
        </div>
      </div>


      {/* Badges Section */}
      <Achievements />

      {/* Theme Setting */}
      <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-4 shadow-sm flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className={`w-10 h-10 rounded-full flex items-center justify-center ${theme === 'dark' ? 'bg-zinc-800 text-yellow-500' : 'bg-yellow-500/20 text-yellow-500'}`}>
            {theme === 'dark' ? <Moon size={20} /> : <Sun size={20} />}
          </div>
          <div>
            <h3 className="font-bold text-white text-sm">مظهر التطبيق</h3>
            <p className="text-[10px] text-zinc-400">
              {theme === 'dark' ? 'الوضع الليلي مفعل' : 'الوضع النهاري مفعل'}
            </p>
          </div>
        </div>
        <button 
          onClick={toggleTheme}
          className={`w-14 h-7 rounded-full transition-colors relative flex items-center shadow-inner ${theme === 'dark' ? 'bg-zinc-700' : 'bg-yellow-500'}`}
        >
          <div className={`w-5 h-5 rounded-full bg-white absolute top-1 shadow-md transition-transform ${theme === 'dark' ? 'right-1' : 'left-1'}`}></div>
        </button>
      </div>

      {/* Settings Options */}
      <div className="space-y-2">
        <h4 className="font-bold text-zinc-400 text-sm px-2 mb-2">الإعدادات</h4>
        
        <button 
          onClick={() => alert("قريباً: تعديل الملف الشخصي")}
          className="w-full bg-zinc-900 hover:bg-zinc-800 border border-zinc-800/50 p-4 rounded-xl flex items-center justify-between transition-colors"
        >
          <span className="text-sm text-white font-medium">الملف الشخصي</span>
          <ChevronLeft size={16} className="text-zinc-600" />
        </button>

        <NotificationSettings />

        <button 
          onClick={() => alert("العربية هي اللغة الوحيدة المتاحة حالياً.")}
          className="w-full bg-zinc-900 hover:bg-zinc-800 border border-zinc-800/50 p-4 rounded-xl flex items-center justify-between transition-colors"
        >
          <span className="text-sm text-white font-medium">اللغة (العربية)</span>
          <ChevronLeft size={16} className="text-zinc-600" />
        </button>

        <button 
          onClick={() => alert("تطبيق أنصار شباب أهلي برج بوعريريج - الإصدار 1.0")}
          className="w-full bg-zinc-900 hover:bg-zinc-800 border border-zinc-800/50 p-4 rounded-xl flex items-center justify-between transition-colors"
        >
          <span className="text-sm text-white font-medium">عن التطبيق</span>
          <ChevronLeft size={16} className="text-zinc-600" />
        </button>
      </div>
      
      <button 
        onClick={() => {
          alert("تم تسجيل الخروج بنجاح");
          window.location.reload();
        }}
        className="w-full text-red-400 text-sm font-bold p-4 bg-zinc-900 rounded-xl hover:bg-red-400/10 transition-colors"
      >
        تسجيل الخروج
      </button>

    </div>
  );
}
