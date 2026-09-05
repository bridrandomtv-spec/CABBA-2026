const fs = require('fs');
let code = fs.readFileSync('src/components/Profile.tsx', 'utf-8');

code = code.replace(
`      await updateProfile(currentUser, {
        displayName: editName,
        photoURL: finalAvatar
      });
      
      const userRef = doc(db, 'users', currentUser.uid);
      await updateDoc(userRef, {
        displayName: editName,
        photoURL: finalAvatar
      });`,
`      const res = await fetch('/api/auth/profile', {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ displayName: editName, avatarUrl: finalAvatar })
      });
      if (!res.ok) throw new Error('فشل تحديث الملف الشخصي');
      if (typeof (window as any).refreshUser === 'function') {
        await (window as any).refreshUser();
      }`
);

// We need to call refreshUser from useAuth.
// Wait, is refreshUser available in Profile.tsx?
// Let's check `const { currentUser, userData, logout } = useAuth();`
