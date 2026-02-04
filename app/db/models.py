from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from app.db.base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    dob = Column(DateTime, default=datetime.now())
