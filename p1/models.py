import os
from datetime import datetime

from peewee import (
    BooleanField, CharField, DateTimeField, ForeignKeyField, Model as PeeweeModel,
    SqliteDatabase, TextField,
)

db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'db.sqlite'))
db = SqliteDatabase(db_path)


class Model(PeeweeModel):
    class Meta:
        database = db


class User(Model):
    name = CharField(max_length=120, index=True)
    active = BooleanField(default=True, index=True)
    joined = DateTimeField(default=datetime.utcnow)


class Post(Model):
    user = ForeignKeyField(User, backref='posts')
    title = CharField(max_length=200)
    created = DateTimeField(default=datetime.utcnow, index=True)
    text = TextField()


db.connect()
db.create_tables([User, Post])
