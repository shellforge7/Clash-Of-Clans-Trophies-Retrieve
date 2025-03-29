from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from os import path

DATABASE_URI = "sqlite:///trophies.db"

engine = create_engine(DATABASE_URI, echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

def initialize_database():
     if not path.exists("trophies.db"):
          Base.metadata.create_all(engine)
          print("Database initialized.")
     else:
          print("Database already exists.")