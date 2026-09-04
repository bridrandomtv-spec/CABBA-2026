import re

with open("src/components/Profile.tsx", "r") as f:
    content = f.read()

reset_func = """  const handleResetPassword = async () => {
    if (!email) {
      alert('الرجاء إدخال البريد الإلكتروني أولاً');
      return;
    }
    try {
      await sendPasswordResetEmail(auth, email);
      alert('تم إرسال رابط إعادة تعيين كلمة المرور إلى بريدك الإلكتروني.');
    } catch (error: any) {
      console.error(error);
      alert('حدث خطأ. تأكد من صحة البريد الإلكتروني.');
    }
  };"""

content = content.replace("  const handleAuth = (e: React.FormEvent) => {", reset_func + "\n\n  const handleAuth = (e: React.FormEvent) => {")

with open("src/components/Profile.tsx", "w") as f:
    f.write(content)
