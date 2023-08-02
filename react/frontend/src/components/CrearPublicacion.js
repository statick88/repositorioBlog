import React from 'react';
import axios from 'axios';

const CrearPublicacion = () => {
  const [titulo, setTitulo] = React.useState('');
  const [contenido, setContenido] = React.useState('');

  // Replace "1" with the ID of the author you want to associate with the publicación
  const autorId = 1;

  const handleCrear = async () => {
    try {
      await axios.post('http://localhost:8000/publicaciones/', {
        titulo,
        contenido,
        autor: autorId,
      });
      alert('Publicación creada correctamente.');
      setTitulo('');
      setContenido('');
    } catch (error) {
      console.error('Error al crear la publicación:', error);
    }
  };

  return (
    <div>
      <h1>Crear Publicación</h1>
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
      <button onClick={handleCrear}>Crear</button>
    </div>
  );
};

export default CrearPublicacion;


