from src.modelo.declarative_base import engine, Base


class Coleccion():

    def __init__(self):
        Base.metadata.create_all(engine)

    def darAlbumes(self):
        pass

    def darCanciones(self):
        pass

    def darInterpretes(self):
        pass

    def buscarAlbumesPorTitulo(self):
        pass

    def buscarCancionesPorTitulo(self):
        pass

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

    def eliminarCancion(self):
        pass

    def eliminarInterprete(self):
        pass

    def editarAlbum(self):
        pass

    def editarCancion(self):
        pass

    def editarInterprete(self):
        pass
