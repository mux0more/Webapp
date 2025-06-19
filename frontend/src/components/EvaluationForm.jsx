import React, { useState } from 'react';

const EvaluationForm = ({ onSubmit, criteria, title }) => {
  const [ratings, setRatings] = useState({});

  const handleChange = (criterion, value) => {
    setRatings({ ...ratings, [criterion]: value });
  };

  const handleSubmit = () => {
    onSubmit(ratings);
  };

  return (
    <div className="bg-white p-4 rounded shadow">
      <h2 className="text-xl font-semibold mb-4">{title}</h2>
      {criteria.map((criterion) => (
        <div key={criterion} className="mb-4">
          <label className="block text-gray-700">{criterion}</label>
          <select
            className="mt-1 p-2 border rounded w-full"
            onChange={(e) => handleChange(criterion, e.target.value)}
          >
            <option value="">Выберите оценку</option>
            {[1, 2, 3, 4, 5].map((score) => (
              <option key={score} value={score}>{score}</option>
            ))}
          </select>
        </div>
      ))}
      <button
        className="bg-blue-500 text-white p-2 rounded w-full"
        onClick={handleSubmit}
      >
        Отправить
      </button>
    </div>
  );
};

export default EvaluationForm;