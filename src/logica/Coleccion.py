from src.modelo import Cancion
from src.modelo.declarative_base import session, engine, Base


class Coleccion():

    def __init__(self):
        Base.metadata.create_all(engine)

    def darAlbumes(self):
        pass

    def darCanciones(self, album_id):
        canciones = session.query(Cancion).filter(Cancion.album_id == album_id).all()
        return canciones

    def darInterpretes(self):
        pass

    def buscarAlbumesPorTitulo(self):
        pass

    def buscarCancionesPorTitulo(self, cancion_titulo):
        canciones = session.query(Cancion).filter((Cancion.titulo).lower() == cancion_titulo.lower()).all()
        return canciones

    def buscarCancionesPorInterprete(self):
        pass

    def agregarAlbum(self):
        pass

    def agregarCancion(self):
        pass

    def agregarInterprete(self):
        pass

    def eliminarAlbum(self):
        pass

    def eliminarCancion(self, cancion_id):
        cancion = session.query(Cancion).filter(Cancion.id == cancion_id).all()[0]
        session.delete(cancion)
        session.commit()

    def eliminarInterprete(self):
        pass

    def editarAlbum(self):
        pass

    def editarCancion(self):
        pass

    def editarInterprete(self):
        pass
