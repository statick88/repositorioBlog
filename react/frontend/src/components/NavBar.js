import React from 'react';
import { Link } from 'react-router-dom';
import '../styles.css'; // Import the custom CSS file

const NavBar = () => {
  return (
    <nav className="navbar navbar-expand navbar-dark bg-dark">
      <div className="container">
        <Link to="/" className="navbar-brand">
          Mi Blog
        </Link>
        <ul className="navbar-nav ml-auto">
          <li className="nav-item">
            <Link to="/" className="nav-link">
              Home
            </Link>
          </li>
          <li className="nav-item">
            <Link to="/contacto" className="nav-link">
              Contacto
            </Link>
          </li>
          <li className="nav-item">
            <Link to="/quienes_somos" className="nav-link">
              Quienes Somos
            </Link>
          </li>
          <li className="nav-item">
            <Link to="/publicaciones/crear" className="nav-link">
              Crear
            </Link>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default NavBar;
