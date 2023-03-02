from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config


DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_NAME = config('DB_NAME')

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/{DB_NAME}", echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Appartment(Base):
    __tablename__ = "appartments"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    currency = Column(String(255))
    price = Column(String(255))
    date = Column(String(255))
    location = Column(String(255))
    image = Column(String(255))


Base.metadata.create_all(engine)
