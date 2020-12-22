from src.modelo.album import Album
from src.modelo.cancion import Cancion
from src.modelo.declarative_base import session, engine, Base
from src.modelo.interprete import Interprete


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
        interpretes = session.query(Interprete).all()
        return interpretes

    def buscarAlbumesPorTitulo(self, album_titulo):
        albumes = session.query(Album).filter(Album.titulo.ilike(album_titulo)).all()
        return albumes

    def buscarCancionesPorTitulo(self, cancion_titulo):
        canciones = session.query(Cancion).filter(Cancion.titulo.ilike(cancion_titulo)).all()
        return canciones

    def buscarCancionesPorInterprete(self, nombre):
        resultado = []
        canciones = session.query(Cancion).all()
        for cancion in canciones:
            for interprete in cancion.interpretes:
                if interprete.nombre == nombre:
                    resultado.append(cancion)
        return resultado

    def agregarAlbum(self, titulo, anio, descripcion, medio):
        try:
            album = Album(titulo=titulo, ano=anio, descripcion=descripcion, medio=medio)
            session.add(album)
            session.commit()
            return True
        except:
            return False

    def agregarCancion(self, titulo, minutos, segundos, compositor, album_id, interpretes_id):
        busqueda = session.query(Cancion).filter(Cancion.albumes.any(Album.id.in_([album_id])),
                                                 Cancion.titulo == titulo).all()
        if len(busqueda) == 0:
            album = session.query(Album).filter(Album.id == album_id).all()[0]
            interpretesCancion = []
            for item in interpretes_id:
                interprete = session.query(Interprete).filter(Interprete.id == item).all()[0]
                interpretesCancion.append(interprete)
            nuevaCancion = Cancion(titulo=titulo, minutos=minutos, segundos=segundos, compositor=compositor,
                                   albumes=[album], interpretes=interpretesCancion)
            session.add(nuevaCancion)
            session.commit()
            return True
        else:
            return False

    def agregarInterprete(self, nombre):
        interprete = session.query(Interprete).filter(Interprete.nombre == nombre).all()
        if len(interprete) == 0:
            nuevoInterprete = Interprete(nombre=nombre)
            session.add(nuevoInterprete)
            session.commit()
            return True
        else:
            return False

    def eliminarAlbum(self, album_id):
        try:
            album = session.query(Album).filter(Album.id == album_id).all()[0]
            session.delete(album)
            session.commit()
            return True
        except:
            return False

    def eliminarCancion(self, cancion_id, album_id):
        try:
            cancion = session.query(Cancion).filter(Cancion.id == cancion_id).all()[0]
            album = session.query(Album).filter(Album.id == album_id).all()[0]
            if len(cancion.albumes) == 1:
                session.delete(cancion)
            elif len(cancion.albumes) > 1:
                album.canciones.remove(cancion)
            session.commit()
            return True
        except:
            return False

    def eliminarInterprete(self, interprete_id):
        interprete = session.query(Interprete).filter(Interprete.id == interprete_id).all()
        if len(interprete) > 0:
            if interprete[0].cancion is None:
                session.delete(interprete[0])
                session.commit()
                return True
            else:
                return False
        else:
            return False

    def editarAlbum(self, album_id, titulo, anio, descripcion, medio):
        try:
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
            return True
        except:
            return False

    def editarCancion(self, cancion_id, titulo, minutos, segundos, compositor,album_id, interpretes_id):
        busqueda = session.query(Cancion).filter(Cancion.albumes.any(Album.id.in_([album_id])),
                                                 Cancion.titulo == titulo, Cancion.id != cancion_id).all()
        if len(busqueda) == 0:
            cancion = session.query(Cancion).filter(Cancion.id == cancion_id).all()[0]
            cancion.titulo = titulo
            cancion.minutos = minutos
            cancion.segundos = segundos
            cancion.compositor = compositor
            interpretesCancion = []
            for item in interpretes_id:
                interprete = session.query(Interprete).filter(Interprete.id == item).all()[0]
                interpretesCancion.append(interprete)
            cancion.interpretes = interpretesCancion
            session.commit()
            return True
        else:
            return False

    def editarInterprete(self, interprete_id, nombre):
        busqueda = session.query(Interprete).filter(Interprete.id != interprete_id, Interprete.nombre == nombre).all()
        if len(busqueda) == 0:
            interprete = session.query(Interprete).filter(Interprete.id == interprete_id).all()[0]
            interprete.nombre = nombre
            session.commit()
            return True
        else:
            return False
