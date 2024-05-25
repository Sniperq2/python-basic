import os
from pathlib import Path

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"
BASE_DIR = Path(__file__).resolve().parent
DB_ECHO = False

async_engine = create_async_engine(
    PG_CONN_URI,
    echo=False,
)

async_session = async_sessionmaker(
    bind=async_engine,
    autocommit=False,
    expire_on_commit=False,
)
