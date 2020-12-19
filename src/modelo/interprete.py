from sqlalchemy import Column, Integer, String, ForeignKey

from .declarative_base import Base


class Interprete(Base):
    __tablename__ = 'interprete'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    cancion_id=Column(Integer, ForeignKey('cancion.id'))

    def __init__(self, nombre):
        self.nombre = nombre
