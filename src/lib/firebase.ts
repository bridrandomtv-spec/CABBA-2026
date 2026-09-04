import { initializeApp } from 'firebase/app';
import { getFirestore } from 'firebase/firestore';
import { getAuth } from 'firebase/auth';
import { getStorage } from 'firebase/storage';

const firebaseConfig = {
  projectId: "project-d6a21fef-1fa2-48c3-86b",
  appId: "1:290720580922:web:811a518a583569fde8bc03",
  apiKey: "AIzaSyCLK9ESvw1VZSMtToeQAqMg1tvWKeY9IKE",
  authDomain: "project-d6a21fef-1fa2-48c3-86b.firebaseapp.com",
  storageBucket: "project-d6a21fef-1fa2-48c3-86b.firebasestorage.app",
  messagingSenderId: "290720580922",
  measurementId: ""
};

const app = initializeApp(firebaseConfig);
export const db = getFirestore(app, "ai-studio-cabba2026-2800937f-914a-44ce-8ee2-609d92fa9cee");
export const auth = getAuth(app);
export const storage = getStorage(app);
