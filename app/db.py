from collections.abc import AsyncGenerator
import uuid
import datetime
from sqlalchemy import Column, Text, DateTime, ForeignKey, String
from sqlclchemy.dialects.postgresql import UUID
from sqlalchmy.ext.asycnio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, relationship

DATABAS_URL = "sqllite+aiosqlite:///./test.db"


class Posts(DeclarativeBase):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(Text, unique=True)
    caption = Column(Text)
    url = Column(String, nullable=False)
    file_name = Column(String, nullable=False)
    file_type = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
