import React from 'react';
import axios from 'axios';

const DetallePublicacion = ({ match }) => {
  const [publicacion, setPublicacion] = React.useState(null);

  React.useEffect(() => {
    const fetchPublicacion = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/publicaciones/${match.params.id}/`
        );
        setPublicacion(response.data);
      } catch (error) {
        console.error('Error al obtener la publicación:', error);
      }
    };

    fetchPublicacion();
  }, [match.params.id]);

  if (!publicacion) {
    return <div>Cargando...</div>;
  }

  return (
    <div>
      <h1>{publicacion.titulo}</h1>
      <p>{publicacion.contenido}</p>
    </div>
  );
};

export default DetallePublicacion;
