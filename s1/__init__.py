"""SQLAlchemy (declarative ORM)
"""
import os
from datetime import datetime

from faker import Faker
from memory_profiler import profile

from .models import Post, Session, User

fake = Faker()


@profile
def populate(num_people: int, num_posts: int):
    t0 = datetime.utcnow()
    session = Session()
    for _ in range(num_people):
        user = User(
            name=fake.name(), active=fake.pybool(),
            joined=fake.past_datetime(start_date='-120d'),
        )
        session.add(user)
        for _ in range(num_posts):
            post = Post(
                user=user, title=fake.sentence(),
                text=fake.paragraph(nb_sentences=9),
            )
            session.add(post)
    session.commit()
    elapsed = datetime.utcnow() - t0
    elapsed = elapsed.total_seconds()
    print(f'total time: {elapsed}')


def clean():
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'db.sqlite'))
    os.unlink(db_path)
