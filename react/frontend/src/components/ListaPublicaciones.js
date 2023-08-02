import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ListaPublicaciones = () => {
  const [publicaciones, setPublicaciones] = useState([]);

  useEffect(() => {
    const fetchPublicaciones = async () => {
      try {
        const response = await axios.get('http://localhost:8000/publicaciones/');
        setPublicaciones(response.data.results);
      } catch (error) {
        console.error('Error al obtener las publicaciones:', error);
      }
    };

    fetchPublicaciones();
  }, []);

  return (
    <div>
      <h1>Lista de Publicaciones</h1>
      <ul>
        {publicaciones.map((publicacion) => (
          <li key={publicacion.id}>
            <h2>{publicacion.titulo}</h2>
            <p>{publicacion.contenido}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ListaPublicaciones;
