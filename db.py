# SQLAlchemy wrapper module

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DataBase(object):
    def __init__(self, url: str) -> None:
        self.Base = Base
        self.engine = create_engine(
            url.replace('postgres://', 'postgresql://'),
            echo=True
        )
        self.session = sessionmaker(bind=self.engine)
        self.s = self.session()

    def add(self, Db, name):
        self.s.add(Db(name))

    def commit(self):
        self.s.commit()

    def close(self):
        self.s.close()

    def getTotal(self, Db):
        first = self.s.query(Db.id).first()
        last = self.s.query(Db.id).order_by(Db.id.desc()).first()
        return (last.id - first.id)
