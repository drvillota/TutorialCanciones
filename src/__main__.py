from src.logica.Coleccion import Coleccion
from src.modelo.album import Album, Medio
from src.modelo.cancion import Cancion
from src.modelo.interprete import Interprete
from src.modelo.declarative_base import session, Base, engine

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    album1= Album(titulo="Probando", ano=1994, descripcion="This is so cool", medio=Medio.DISCO)
    interprete1= Interprete(nombre="Prisioneros")
    cancion1= Cancion(titulo="Test", minutos=3, segundos=40, compositor="X")
    cancion2 = Cancion(titulo="Test2", minutos=3, segundos=40, compositor="X")
    cancion3 = Cancion(titulo="Test3", minutos=3, segundos=40, compositor="X")
    session.add(album1)
    session.add(interprete1)
    session.add(cancion1)
    session.add(cancion2)
    session.add(cancion3)
    session.commit()
    cancion1.albumes = [album1]
    cancion2.albumes = [album1]
    cancion3.albumes = [album1]
    cancion1.interpretes=[interprete1]
    cancion2.interpretes=[interprete1]
    cancion3.interpretes=[interprete1]
    album1.canciones=[cancion1,cancion2,cancion3]
    session.commit()


    print(album1.id)
    print(cancion1.albumes[0].id)
    session.close()
    coleccion = Coleccion()
    print(coleccion.darCanciones(1))
    print(coleccion.buscarCancionesPorTitulo("Test3"))
    coleccion.eliminarCancion(1)
    print(coleccion.darCanciones(1))

