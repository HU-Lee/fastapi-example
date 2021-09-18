from sqlalchemy import Column, Integer, String

from .db_init import Base

class CovidKorea(Base):
    __tablename__ = "tb_covidkor"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String, unique=True)
    detected = Column(Integer)
    death = Column(Integer)

class CovidInter(Base):
    __tablename__ = "tb_covidinter"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String, unique=True)
    jap = Column(Integer)
    usa = Column(Integer)