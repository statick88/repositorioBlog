import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ActualizarPublicacion = () => {
  const [titulo, setTitulo] = useState('');
  const [contenido, setContenido] = useState('');
  const [autor, setAutor] = useState('');

  // Replace "3" with the ID of the publicación you want to update
  const publicacionId = 5;

  useEffect(() => {
    const fetchPublicacion = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/publicaciones/${publicacionId}/`);
        const { titulo, contenido, autor } = response.data;
        setTitulo(titulo);
        setContenido(contenido);
        setAutor(autor);
      } catch (error) {
        console.error('Error al obtener la publicación:', error);
      }
    };

    fetchPublicacion();
  }, [publicacionId]);

  const handleActualizar = async () => {
    try {
      await axios.put(`http://localhost:8000/publicaciones/${publicacionId}/`, {
        titulo,
        contenido,
        autor,
      });
      alert('Publicación actualizada correctamente.');
    } catch (error) {
      console.error('Error al actualizar la publicación:', error);
    }
  };

  return (
    <div>
      <h1>Actualizar Publicación</h1>
      <label>
        Título:
        <input type="text" value={titulo} onChange={(e) => setTitulo(e.target.value)} />
      </label>
      <br />
      <label>
        Contenido:
        <textarea value={contenido} onChange={(e) => setContenido(e.target.value)} />
      </label>
      <br />
      <label>
        Autor:
        <input type="number" value={autor} onChange={(e) => setAutor(Number(e.target.value))} />
      </label>
      <br />
      <button onClick={handleActualizar}>Actualizar</button>
    </div>
  );
};

export default ActualizarPublicacion;
