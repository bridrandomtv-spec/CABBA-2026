import { Droplets, Wind, Sun, MapPin } from 'lucide-react';

export default function WeatherWidget() {
  return (
    <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-4 shadow-sm relative overflow-hidden">
      <div className="absolute top-0 right-0 w-32 h-32 bg-blue-500/5 rounded-full blur-2xl translate-x-10 -translate-y-10"></div>
      
      <div className="flex justify-between items-center mb-4 relative z-10">
        <div className="flex items-center gap-2">
          <h3 className="font-bold text-white text-lg">طقس الملعب</h3>
        </div>
        <div className="flex items-center gap-1.5 bg-zinc-800 px-2 py-1 rounded-lg">
          <MapPin size={12} className="text-zinc-500" />
          <span className="text-[10px] text-zinc-400 font-bold">برج بوعريريج</span>
        </div>
      </div>

      <div className="flex items-center justify-between relative z-10">
        <div className="flex items-center gap-4">
          <div className="w-14 h-14 bg-yellow-500/10 rounded-full flex items-center justify-center text-yellow-500 relative">
            <Sun size={32} className="fill-yellow-500" />
            {/* Sun rays animation effect */}
            <div className="absolute inset-0 bg-yellow-500/20 rounded-full animate-ping opacity-75"></div>
          </div>
          <div>
            <div className="flex items-end gap-1">
              <span className="text-3xl font-black text-white tracking-tighter">22°</span>
              <span className="text-sm font-bold text-zinc-500 mb-1">C</span>
            </div>
            <p className="text-sm font-bold text-yellow-500">مشمس وصافي</p>
          </div>
        </div>

        <div className="flex flex-col gap-2 border-r border-zinc-800 pr-4">
          <div className="flex items-center gap-2 text-xs">
            <Wind size={14} className="text-zinc-500" />
            <span className="text-zinc-400 font-bold">12 كم/س</span>
          </div>
          <div className="flex items-center gap-2 text-xs">
            <Droplets size={14} className="text-zinc-500" />
            <span className="text-zinc-400 font-bold">45%</span>
          </div>
        </div>
      </div>
      
      <div className="mt-4 pt-3 border-t border-zinc-800/50 flex items-center gap-2 text-[10px] text-zinc-400 relative z-10">
        <span className="w-2 h-2 rounded-full bg-green-500"></span>
        <span>الظروف مثالية لإجراء المباراة القادمة في ملعب 20 أوت</span>
      </div>
    </div>
  );
}
