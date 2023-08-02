import React, { useEffect } from 'react';
import axios from 'axios';

const EliminarPublicacion = () => {
  // Replace "2" with the ID of the publicación you want to delete
  const publicacionId = 5;

  useEffect(() => {
    const fetchPublicacion = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/publicaciones/${publicacionId}/`);
        const { titulo, contenido, autor } = response.data;
        console.log('Publicación a eliminar:', { titulo, contenido, autor });
      } catch (error) {
        console.error('Error al obtener la publicación:', error);
      }
    };

    fetchPublicacion();
  }, [publicacionId]);

  const handleEliminar = async () => {
    try {
      await axios.delete(`http://localhost:8000/publicaciones/${publicacionId}/`);
      alert('Publicación eliminada correctamente.');
    } catch (error) {
      console.error('Error al eliminar la publicación:', error);
    }
  };

  return (
    <div>
      <h1>Eliminar Publicación</h1>
      <p>¿Estás seguro de que deseas eliminar esta publicación?</p>
      <button onClick={handleEliminar}>Eliminar</button>
    </div>
  );
};

export default EliminarPublicacion;
