import React, { useState } from 'react';

function Skills({ skills, onAddSkill }) {
  const [skillInput, setSkillInput] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (skillInput.trim()) {
      onAddSkill(skillInput.trim());
      setSkillInput('');
    }
  };

  return (
    <div className="card">
      <h2>Student Skills</h2>

      <ul className="skills-list">
        {skills.map((skill, index) => (
          <li key={index} className="skill-tag">
            {skill}
          </li>
        ))}
      </ul>

      <form onSubmit={handleSubmit} className="add-skill-form">
        <input
          type="text"
          className="input-field"
          placeholder="e.g., Python, Docker..."
          value={skillInput}
          onChange={(e) => setSkillInput(e.target.value)}
        />
        <button type="submit">Add Skill</button>
      </form>
    </div>
  );
}

export default Skills;
