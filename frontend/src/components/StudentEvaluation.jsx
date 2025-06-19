import React from 'react';
import EvaluationForm from './EvaluationForm';

const StudentEvaluation = ({ user }) => {
  const criteria = ['Ясность', 'Поддержка', 'Экспертиза', 'Доступность'];
  
  const handleSubmit = async (ratings) => {
    try {
      const response = await fetch('http://localhost:8000/evaluate/teacher', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ userId: user.id, ratings }),
      });
      if (response.ok) {
        window.Telegram.WebApp.showAlert('Оценка отправлена!');
      } else {
        window.Telegram.WebApp.showAlert('Ошибка при отправке оценки.');
      }
    } catch (error) {
      window.Telegram.WebApp.showAlert('Ошибка сети.');
    }
  };

  return (
    <EvaluationForm
      onSubmit={handleSubmit}
      criteria={criteria}
      title="Оценка преподавателя"
    />
  );
};

export default StudentEvaluation;