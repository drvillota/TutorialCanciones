from src.logica.Coleccion import Coleccion
from src.modelo.album import Album, Medio
from src.modelo.cancion import Cancion
from src.modelo.interprete import Interprete
from src.modelo.declarative_base import session, Base, engine

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    album1= Album(titulo="Probando", ano=1994, descripcion="This is so cool", medio=Medio.DISCO)
    album2 = Album(titulo="Probando2", ano=1994, descripcion="This is so cool part 2", medio=Medio.DISCO)
    interprete1= Interprete(nombre="Prisioneros")
    cancion1= Cancion(titulo="Test", minutos=3, segundos=40, compositor="X")
    cancion2 = Cancion(titulo="Test2", minutos=3, segundos=40, compositor="X")
    cancion3 = Cancion(titulo="Test3", minutos=3, segundos=40, compositor="X")
    session.add(album1)
    session.add(album2)
    session.add(interprete1)
    session.add(cancion1)
    session.add(cancion2)
    session.add(cancion3)
    session.commit()
    cancion1.albumes = [album1, album2]
    cancion2.albumes = [album1]
    cancion3.albumes = [album1]
    cancion1.interpretes=[interprete1]
    cancion2.interpretes=[interprete1]
    cancion3.interpretes=[interprete1]
    album1.canciones=[cancion1,cancion2,cancion3]
    album2.canciones = [cancion1]
    session.commit()


    print(album2.id)
    print(cancion1.id)

    coleccion = Coleccion()
    print(coleccion.darCanciones(1))
    print(coleccion.darCanciones(2))
    print(coleccion.buscarCancionesPorTitulo("Test3"))
    coleccion.eliminarCancion(1,1)
    print('Albumes con canciones')
    print(coleccion.darCanciones(1))
    print(coleccion.darCanciones(2))
    print(album2.canciones[0].id)
    coleccion.editarAlbum(2, "", None, "Descripcion editado", Medio.CASETE)
    print(album2.titulo)
    print(album2.descripcion)
    print(album2.medio)
    session.close()
    coleccion.agregarAlbum('Título',1994,'New álbum',Medio.CASETE)
    print(coleccion.darAlbumes())
