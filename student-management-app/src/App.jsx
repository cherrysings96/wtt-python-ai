import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import Student from './components/Student';
import Skills from './components/Skills';

function App() {
  // 1. Manage student state with useState
  const [student, setStudent] = useState({
    name: 'Rahul Sharma',
    age: 20,
    skills: ['React', 'JavaScript', 'HTML/CSS']
  });

  // 2. useEffect to log message when the component loads
  useEffect(() => {
    console.log("Student Management App Loaded");
  }, []);

  // Handlers for state updates
  const handleIncreaseAge = () => {
    setStudent(prev => ({
      ...prev,
      age: prev.age + 1
    }));
  };

  const handleChangeName = (newName) => {
    setStudent(prev => ({
      ...prev,
      name: newName
    }));
  };

  const handleAddSkill = (newSkill) => {
    if (!student.skills.includes(newSkill)) {
      setStudent(prev => ({
        ...prev,
        skills: [...prev.skills, newSkill]
      }));
    }
  };

  return (
    <div>
      {/* Navbar Component */}
      <Navbar />

      <main className="container">
        {/* Student Component with Props */}
        <Student
          name={student.name}
          age={student.age}
          onIncreaseAge={handleIncreaseAge}
          onChangeName={handleChangeName}
        />

        {/* Skills Component with Props */}
        <Skills
          skills={student.skills}
          onAddSkill={handleAddSkill}
        />
      </main>
    </div>
  );
}

export default App;
