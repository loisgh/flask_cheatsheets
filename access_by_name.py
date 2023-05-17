from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Names(Base):
    __tablename__ = 'namesapi_names'
    id = Column(Integer, primary_key=True)
    first = Column(String)
    last = Column(String)
    email = Column(String)


def get_name(id:int, dbPath:str):

    engine = create_engine(dbPath)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session.query(Names).filter(Names.id.__eq__(id)).all()


