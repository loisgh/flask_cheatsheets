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


def get_name(id: int):

    dbPath ='sqlite:///db.sqlite3'
    engine = create_engine(dbPath, echo=True)

    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    names = session.query(Names).filter(Names.id.__eq__(id)).all()

    return names


if __name__ == "__main__":
    get_name(1)