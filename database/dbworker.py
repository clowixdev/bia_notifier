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
            noti_status=userdata[1],
            noti_remind=userdata[2],
            noti_dayinfo=userdata[3],
            noti_weekends=userdata[4],
            noti_visibility=userdata[5]
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


def turn_noti_on(user_id: int, engine: Engine) -> None:
    session = create_session(engine)
    user = []
    try:
        if user_id != None:
            user = session.query(User).filter_by(id=user_id).first()
            if not user:
                return None
        user.noti_status = 1
        
        session.add(user)
        session.commit()
    except BaseException as e:
        print(e)
        session.rollback()
    finally:
        session.close()


def turn_noti_off(user_id: int, engine: Engine) -> None:
    session = create_session(engine)
    user = []
    try:
        if user_id != None:
            user = session.query(User).filter_by(id=user_id).first()
            if not user:
                return None
        user.noti_status = 0

        session.add(user)
        session.commit()
    except BaseException as e:
        print(e)
        session.rollback()
    finally:
        session.close()


def turn_dayinfo_on(user_id: int, engine: Engine) -> None:
    session = create_session(engine)
    user = []
    try:
        if user_id != None:
            user = session.query(User).filter_by(id=user_id).first()
            if not user:
                return None
        user.noti_dayinfo = 1

        session.add(user)
        session.commit()
    except BaseException as e:
        print(e)
        session.rollback()
    finally:
        session.close()


def turn_dayinfo_off(user_id: int, engine: Engine) -> None:
    session = create_session(engine)
    user = []
    try:
        if user_id != None:
            user = session.query(User).filter_by(id=user_id).first()
            if not user:
                return None
        user.noti_dayinfo = 0

        session.add(user)
        session.commit()
    except BaseException as e:
        print(e)
        session.rollback()
    finally:
        session.close()


def turn_visibility_on(user_id: int, engine: Engine) -> None:
    session = create_session(engine)
    user = []
    try:
        if user_id != None:
            user = session.query(User).filter_by(id=user_id).first()
            if not user:
                return None
        user.noti_visibility = 1

        session.add(user)
        session.commit()
    except BaseException as e:
        print(e)
        session.rollback()
    finally:
        session.close()


def turn_visibility_off(user_id: int, engine: Engine) -> None:
    session = create_session(engine)
    user = []
    try:
        if user_id != None:
            user = session.query(User).filter_by(id=user_id).first()
            if not user:
                return None
        user.noti_visibility = 0

        session.add(user)
        session.commit()
    except BaseException as e:
        print(e)
        session.rollback()
    finally:
        session.close()


def update_user_weekends(user_id: int, engine: Engine, weekends: str) -> None:
    session = create_session(engine)
    user = []
    try:
        if user_id != None:
            user = session.query(User).filter_by(id=user_id).first()
            if not user:
                return None
        user.noti_weekends = "".join([day for day in weekends if day != "0"])

        session.add(user)
        session.commit()
    except BaseException as e:
        print(e)
        session.rollback()
    finally:
        session.close()


def set_dayinfo_time(user_id: int, engine: Engine, dayinfo_time: int) -> None:
    session = create_session(engine)
    user = []
    try:
        if user_id != None:
            user = session.query(User).filter_by(id=user_id).first()
            if not user:
                return None
        user.noti_dayinfo = dayinfo_time

        session.add(user)
        session.commit()
    except BaseException as e:
        print(e)
        session.rollback()
    finally:
        session.close()


def set_remind_time(user_id: int, engine: Engine, remind_time: int) -> None:
    session = create_session(engine)
    user = []
    try:
        if user_id != None:
            user = session.query(User).filter_by(id=user_id).first()
            if not user:
                return None
        user.noti_remind = remind_time

        session.add(user)
        session.commit()
    except BaseException as e:
        print(e)
        session.rollback()
    finally:
        session.close()