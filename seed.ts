import { initializeApp } from 'firebase/app';
import { getFirestore, collection, addDoc, getDocs } from 'firebase/firestore';

const firebaseConfig = {
  projectId: "project-d6a21fef-1fa2-48c3-86b",
  appId: "1:290720580922:web:811a518a583569fde8bc03",
  apiKey: "AIzaSyCLK9ESvw1VZSMtToeQAqMg1tvWKeY9IKE",
  authDomain: "project-d6a21fef-1fa2-48c3-86b.firebaseapp.com",
  storageBucket: "project-d6a21fef-1fa2-48c3-86b.firebasestorage.app",
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app, "ai-studio-cabba2026-2800937f-914a-44ce-8ee2-609d92fa9cee");

const DEFAULT_POSTS = [
  {
    author: 'أحمد الكاباوي',
    avatar: 'A',
    time: 'قبل ساعتين',
    content: 'أجواء رائعة اليوم في المدرجات! الفريق قدم أداء خرافي، النقاط الثلاث هي الأهم. الجراد الأصفر دائماً في الموعد 💛🖤',
    likes: 124,
    comments: 18,
    createdAt: Date.now() - 7200000
  },
  {
    author: 'رياض 34',
    avatar: 'R',
    time: 'قبل 4 ساعات',
    content: 'صور من دخلة اليوم.. الإبداع مستمر!',
    imageUrl: 'https://images.unsplash.com/photo-1508344928928-7137b29de216?auto=format&fit=crop&q=80&w=800&h=400',
    likes: 342,
    comments: 45,
    createdAt: Date.now() - 14400000
  },
  {
    author: 'وليد BBA',
    avatar: 'W',
    time: 'قبل 5 ساعات',
    content: 'من هو رجل المباراة برأيكم؟ بالنسبة لي الحارس كان سداً منيعاً.',
    likes: 89,
    comments: 112,
    createdAt: Date.now() - 18000000
  }
];

async function seed() {
  const querySnapshot = await getDocs(collection(db, 'posts'));
  if (querySnapshot.empty) {
    for (const post of DEFAULT_POSTS) {
      await addDoc(collection(db, 'posts'), post);
    }
    console.log('Seeded database');
  } else {
    console.log('Database already has data');
  }
}

seed().catch(console.error);
