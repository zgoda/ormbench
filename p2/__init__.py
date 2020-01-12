"""Pony ORM
"""
import os
from datetime import datetime

from faker import Faker
from memory_profiler import profile
from pony.orm import db_session

from .models import Post, User

fake = Faker()


@profile
def populate(num_people: int, num_posts: int):
    t0 = datetime.utcnow()
    with db_session:
        for _ in range(num_people):
            user = User(
                name=fake.name(), active=fake.pybool(),
                joined=fake.past_datetime(start_date='-120d'),
            )
            for _ in range(num_posts):
                Post(
                    user=user, title=fake.sentence(),
                    text=fake.paragraph(nb_sentences=9),
                )
    elapsed = datetime.utcnow() - t0
    elapsed = elapsed.total_seconds()
    print(f'total time: {elapsed}')


def clean():
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'db.sqlite'))
    os.unlink(db_path)
