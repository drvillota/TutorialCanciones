from src.logica.Coleccion import Coleccion
from src.modelo.album import Album, Medio
from src.modelo.cancion import Cancion
from src.modelo.interprete import Interprete
from src.modelo.declarative_base import session, Base, engine

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session.close()
