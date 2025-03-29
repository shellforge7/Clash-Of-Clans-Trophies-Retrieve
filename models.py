from database import Base
from sqlalchemy import Column, Integer
import time

class Trophy(Base):
     __tablename__ = 'trophies'

     id = Column(Integer, primary_key=True, autoincrement=True)
     trophies = Column(Integer, nullable=False)
     time = Column(Integer, nullable=False, default=int(time.time()))