import re

with open("src/components/Profile.tsx", "r") as f:
    content = f.read()

# Remove language alerts
content = re.sub(r"    if \(lang === 'fr'\) \{.*?\}\n", "", content, flags=re.DOTALL)

# Add sendPasswordResetEmail to imports
if "sendPasswordResetEmail" not in content:
    content = content.replace("import { updateProfile", "import { updateProfile, sendPasswordResetEmail")

# Implement reset password
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

if "const handleResetPassword" not in content:
    content = content.replace("  const handleAuth = async (e: React.FormEvent) => {", reset_func + "\n\n  const handleAuth = async (e: React.FormEvent) => {")

content = content.replace("onClick={() => alert('سيتم إرسال رابط إعادة تعيين كلمة المرور.')}", "onClick={handleResetPassword}")

# Remove dead buttons
content = re.sub(r"\s*<button onClick=\{\(\) => alert\('هذه الخاصية ستتوفر قريباً!'\)\}.*?>\s*<div className=\"flex items-center gap-3\">\s*<Shield.*?>.*?</span>\s*</div>\s*<ChevronLeft.*?>\s*</button>", "", content, flags=re.DOTALL)

content = re.sub(r"\s*<button onClick=\{\(\) => alert\('هذه الخاصية ستتوفر قريباً!'\)\}.*?>\s*<div className=\"flex items-center gap-3\">\s*<CheckCircle2.*?>.*?</span>\s*</div>\s*<ChevronLeft.*?>\s*</button>", "", content, flags=re.DOTALL)


with open("src/components/Profile.tsx", "w") as f:
    f.write(content)
