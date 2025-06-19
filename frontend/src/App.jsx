import React, { useState, useEffect } from 'react';
import './App.css';
import EvaluationForm from './components/EvaluationForm';
import TeacherEvaluation from './components/TeacherEvaluation';
import StudentEvaluation from './components/StudentEvaluation';

const App = () => {
  const [user, setUser] = useState(null);
  const [role, setRole] = useState(null);

  useEffect(() => {
    const tg = window.Telegram?.WebApp;
    if (tg) {
      tg.ready(); // Инициализация Telegram Web App
      const initData = tg.initDataUnsafe || {};
      setUser(initData.user || null);
      setRole(initData.user?.id % 2 === 0 ? 'teacher' : 'student');
    } else {
      console.error('Telegram WebApp is not available');
      // Опционально: задайте тестовые данные для отладки
      setUser({ id: 123, first_name: 'Test User' });
      setRole('student');
    }
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <h1 className="text-2xl font-bold text-center mb-4">Приложение для оценок</h1>
      {user && role ? (
        role === 'teacher' ? (
          <TeacherEvaluation user={user} />
        ) : (
          <StudentEvaluation user={user} />
        )
      ) : (
        <p>Загрузка...</p>
      )}
    </div>
  );
};

export default App;