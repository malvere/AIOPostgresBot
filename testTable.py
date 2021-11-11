# SQLAlchemy Table for test purposes

from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import VARCHAR

Base = declarative_base()


class TestTable(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(50), nullable=False, unique=True)

    def __init__(self, availUsername):
        self.username = availUsername

    def __repr__(self):
        return f'username = {self.username} with id = {self.id}.'
