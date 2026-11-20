import React, { useState } from 'react';

function Student({ name, age, onIncreaseAge, onChangeName }) {
  const [isEditing, setIsEditing] = useState(false);
  const [newName, setNewName] = useState(name);

  const handleSaveName = (e) => {
    e.preventDefault();
    if (newName.trim()) {
      onChangeName(newName.trim());
      setIsEditing(false);
    }
  };

  return (
    <div className="card">
      <h2>Student Details</h2>

      <div className="info-row">
        <span><strong>Student Name:</strong> {name}</span>
      </div>

      <div className="info-row">
        <span><strong>Student Age:</strong> {age} years old</span>
      </div>

      {isEditing ? (
        <form onSubmit={handleSaveName} style={{ display: 'flex', gap: '8px', marginBottom: '16px' }}>
          <input
            type="text"
            className="input-field"
            value={newName}
            onChange={(e) => setNewName(e.target.value)}
            placeholder="Enter new name"
            autoFocus
          />
          <button type="submit">Save</button>
          <button
            type="button"
            className="btn-secondary"
            onClick={() => {
              setNewName(name);
              setIsEditing(false);
            }}
          >
            Cancel
          </button>
        </form>
      ) : null}

      <div className="btn-group">
        <button onClick={onIncreaseAge}>Increase Age</button>
        {!isEditing && (
          <button className="btn-secondary" onClick={() => setIsEditing(true)}>
            Change Name
          </button>
        )}
      </div>
    </div>
  );
}

export default Student;
