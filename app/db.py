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


engine = create_async_engine(DATABAS_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def create_db_and_table():
    async with engine.begin() as conn:
        await conn.run_sync(DeclarativeBase.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_sessionmaker() as session:
        yield session
