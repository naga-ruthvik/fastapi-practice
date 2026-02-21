from sqlalchemy import Column, String, Integer, DateTime, Enum, ForeignKey
from datetime import datetime
from app.db.base import Base
import enum


# ENUMS -> STORES ALL ENUMS USED FOR MODELS --------------


class ProjectType(enum.Enum):
    COMPUTER_SCIENCE = "COMPUTER SCIENCE"
    ELECTRICAL = "ELECTRICAL"
    MECHANICAL = "MECHANICAL"
    ARTIFICIAL_INTELLIGENCE = "ARTIFICICAL INTELLIGENCE"


# MAIN MODELS -> USES TABLES USED IN MAIN DATABASE -----------------


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    dob = Column(DateTime, default=datetime.now())


class Projects(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    project_type = Column(Enum(ProjectType), nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
