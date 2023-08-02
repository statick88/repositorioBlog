// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import NavBar from './components/NavBar'; // Corrected import path
import ListaPublicaciones from './components/ListaPublicaciones';
import CrearPublicacion from './components/CrearPublicacion';
import DetallePublicacion from './components/DetallePublicacion';
import ActualizarPublicacion from './components/ActualizarPublicacion';
import EliminarPublicacion from './components/EliminarPublicacion';
import './index.css'; // Importar index.css aquí
import './App.css'; // Importar App.css aquí

const App = () => {
  return (
    <Router>
      <div>
      <NavBar />
        <Routes>
            <Route path="/" element={<ListaPublicaciones />} />
            <Route path="/crear" element={<CrearPublicacion />} />
            <Route path="/:id" element={<DetallePublicacion />} />
            <Route path="/:id/actualizar" element={<ActualizarPublicacion />} />
            <Route path="/:id/eliminar" element={<EliminarPublicacion />} />
          </Routes>
        </div>
      </Router>
  );
};

export default App;
