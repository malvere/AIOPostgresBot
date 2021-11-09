from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import VARCHAR

Base = declarative_base()


class AvailName(Base):
    __tablename__ = 'avail_names'
    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(50))

    def __init__(self, availUsername):
        self.username = availUsername

    def __repr__(self):
        return f'username = {self.username} with id = {self.id}.'


class DataBase(object):
    def __init__(self, url) -> None:
        self.Base = Base
        self.engine = create_engine(
            url,
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
