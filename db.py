from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://evr:1@localhost:5432/parser", echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Appartment(Base):
    __tablename__ = "appartments"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    price = Column(String(255))
    currency = Column(String(255))
    location = Column(String(255))
    image = Column(String(255))
    date = Column(String(255))


Base.metadata.create_all(engine)
