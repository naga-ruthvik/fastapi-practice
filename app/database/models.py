from sqlalchemy import Column, String, Integer, DateTime
import datetime
from database.db import Base


class User(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    dob = Column(DateTime, default=datetime.now())
