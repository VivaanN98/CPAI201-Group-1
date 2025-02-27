// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import {getFirestore} from "firebase/firestore"
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCZJSFT1koKKXGqMy-4jRuaw5znj8F_h-8",
  authDomain: "tourly-f0eb3.firebaseapp.com",
  projectId: "tourly-f0eb3",
  storageBucket: "tourly-f0eb3.firebasestorage.app",
  messagingSenderId: "638380263910",
  appId: "1:638380263910:web:6a5c01da150b5d9a94ae27",
  measurementId: "G-ZEJK98LZCN"
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);
export const db=getFirestore(app);
// const analytics = getAnalytics(app);