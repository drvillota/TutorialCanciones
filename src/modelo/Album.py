import enum
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .declarative_base import Base


class Medio(enum.Enum):
    DISCO = 1
    CASETE = 2
    CD = 3


class Album(Base):
    __tablename__ = 'album'
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    ano = Column(Integer)
    descripcion = Column(String)
    medio = Column(Medio)
    canciones = relationship('Cancion', secondary='link')
