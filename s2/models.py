import os
from datetime import datetime

from sqlalchemy import (
    Boolean, Column, DateTime, ForeignKey, Integer, MetaData, String, Table, Text,
    create_engine,
)

db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'db.sqlite'))
engine = create_engine(f'sqlite:///{db_path}')

metadata = MetaData()

users = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(120), nullable=False, index=True),
    Column('active', Boolean, default=True),
    Column('joined', DateTime, nullable=False, default=datetime.utcnow),
)


posts = Table(
    'post', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', None, ForeignKey('users.id')),
    Column('title', String(200), nullable=False),
    Column('created', DateTime, default=datetime.utcnow, index=True),
    Column('text', Text, nullable=False),
)

metadata.create_all(engine)
