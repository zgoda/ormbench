import os
from datetime import datetime

from pony.orm import Database, Required, Set

db = Database()


class User(db.Entity):
    name = Required(str, 120, index=True)
    active = Required(bool, default=True, index=True)
    joined = Required(datetime, default=datetime.utcnow)
    posts = Set('Post')


class Post(db.Entity):
    user = Required(User)
    title = Required(str, 200)
    created = Required(datetime, default=datetime.utcnow, index=True)
    text = Required(str)


db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'db.sqlite'))
db.bind(provider='sqlite', filename=db_path, create_db=True)
db.generate_mapping(create_tables=True)
