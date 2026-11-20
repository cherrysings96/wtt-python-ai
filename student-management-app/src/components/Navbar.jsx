import React from 'react';

function Navbar() {
  const navStyle = {
    backgroundColor: '#1e3a8a',
    color: '#ffffff',
    padding: '16px 24px',
    boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
  };

  const titleStyle = {
    fontSize: '1.4rem',
    fontWeight: 'bold',
    maxWidth: '800px',
    margin: '0 auto',
  };

  return (
    <nav style={navStyle}>
      <h1 style={titleStyle}>🎓 Student Management Portal</h1>
    </nav>
  );
}

export default Navbar;
