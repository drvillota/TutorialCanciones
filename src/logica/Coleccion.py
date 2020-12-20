from src.modelo.album import Album
from src.modelo.cancion import Cancion
from src.modelo.declarative_base import session, engine, Base

class Coleccion():

    def __init__(self):
        Base.metadata.create_all(engine)

    def darAlbumes(self):
        albumes = session.query(Album).all()
        return albumes


    def darCanciones(self, album_id):
        canciones = session.query(Cancion).filter(Cancion.albumes.any(Album.id.in_([album_id]))).all()
        return canciones


    def darInterpretes(self):
        pass

    def buscarAlbumesPorTitulo(self, album_titulo):
        albumes = session.query(Album).filter(Album.titulo.ilike(album_titulo)).all()
        return albumes


    def buscarCancionesPorTitulo(self, cancion_titulo):
        canciones = session.query(Cancion).filter(Cancion.titulo.ilike(cancion_titulo)).all()
        return canciones


    def buscarCancionesPorInterprete(self):
        pass

    def agregarAlbum(self, titulo, anio, descripcion, medio):
        album = Album(titulo= titulo, ano= anio, descripcion= descripcion, medio= medio)
        session.add(album)
        session.commit()


    def agregarCancion(self):
        pass

    def agregarInterprete(self):
        pass

    def eliminarAlbum(self, album_id):
        album = session.query(Album).filter(Album.id == album_id).all()[0]
        session.delete(album)
        session.commit()


    def eliminarCancion(self, cancion_id, album_id):
        cancion = session.query(Cancion).filter(Cancion.id == cancion_id).all()[0]
        album = session.query(Album).filter(Album.id == album_id).all()[0]
        if len(cancion.albumes)==1:
            session.delete(cancion)
        elif len(cancion.albumes)>1:
            album.canciones.remove(cancion)
        session.commit()


    def eliminarInterprete(self):
        pass

    def editarAlbum(self, album_id, titulo, anio, descripcion, medio):
        album = session.query(Album).filter(Album.id == album_id).all()[0]
        if titulo:
            album.titulo = titulo
        if anio:
            album.ano = anio
        if descripcion:
            album.descripcion = descripcion
        if medio:
            album.medio = medio
        session.commit()


    def editarCancion(self):
        pass

    def editarInterprete(self):
        pass
