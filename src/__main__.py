from src.modelo.declarative_base import session, Base, engine

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session.close()
