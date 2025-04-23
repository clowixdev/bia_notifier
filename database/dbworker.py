from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from .models import Base, User


def create_db_engine() -> Engine:
    engine = create_engine('sqlite+pysqlite:///database/database.db')
    Base.metadata.create_all(engine)

    return engine


def create_session(engine: Engine) -> Session:
    Session = sessionmaker(bind=engine)
    return Session()