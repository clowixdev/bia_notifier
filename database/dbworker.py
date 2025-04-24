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


def add_user(userdata: list, engine: Engine) -> User:
    session = create_session(engine)
    try:
        user = User(
            id=userdata[0],
            noti_period=userdata[1],
            noti_amount=userdata[2],
            noti_weekends=userdata[3],
            noti_spoiler=userdata[4]
        )

        session.add(user)
        session.commit()
    except BaseException as e:
        print(e)
        session.rollback()
    finally:
        session.close()


def get_user(user_id: Optional[int], engine: Engine) -> User:
    session = create_session(engine)
    user = []
    try:
        if user_id != None:
            user = session.query(User).filter_by(id=user_id).first()
            if not user:
                return None

        session.expunge(user)
    except BaseException as e:
        print(e)
        session.rollback()
    finally:
        session.close()

    return user