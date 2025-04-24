from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    noti_status = Column(Boolean)
    noti_period = Column(Integer)
    noti_amount = Column(Integer)
    noti_weekends = Column(Integer) # 145 - пн, чт, пт
    noti_spoiler = Column(Boolean)