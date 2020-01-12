import os
from datetime import datetime

from sqlalchemy import (
    Boolean, Column, DateTime, ForeignKey, Integer, String, Text, create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship, sessionmaker

db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'db.sqlite'))
engine = create_engine(f'sqlite:///{db_path}')

Session = sessionmaker(bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False, index=True)
    active = Column(Boolean, default=True)
    joined = Column(DateTime, nullable=False, default=datetime.utcnow)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref=backref('posts', lazy='dynamic'))
    title = Column(String(200), nullable=False)
    created = Column(DateTime, default=datetime.utcnow, index=True)
    text = Column(Text, nullable=False)


Base.metadata.create_all(engine)
