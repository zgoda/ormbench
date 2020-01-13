"""PeeWee ORM
"""
from datetime import datetime

from faker import Faker
from memory_profiler import profile

from .models import Post, User, db

fake = Faker()


@profile
def populate(num_people: int = 120, num_posts: int = 60):
    t0 = datetime.utcnow()
    with db.atomic():
        for _ in range(num_people):
            user = User.create(
                name=fake.name(), active=fake.pybool(),
                joined=fake.past_datetime(start_date='-120d'),
            )
            for _ in range(num_posts):
                Post.create(
                    user=user, title=fake.sentence(),
                    text=fake.paragraph(nb_sentences=9),
                )
    elapsed = datetime.utcnow() - t0
    elapsed = elapsed.total_seconds()
    print(f'total time: {elapsed}')


@profile
def insert_one():
    t0 = datetime.utcnow()
    User.create(
        name=fake.name(), active=fake.pybool(),
        joined=fake.past_datetime(start_date='-120d'),
    )
    elapsed = datetime.utcnow() - t0
    elapsed = elapsed.total_seconds()
    print(f'total time: {elapsed}')


@profile
def insert_one_with_related():
    t0 = datetime.utcnow()
    with db.atomic():
        user = User.create(
            name=fake.name(), active=fake.pybool(),
            joined=fake.past_datetime(start_date='-120d'),
        )
        Post.create(
            user=user, title=fake.sentence(),
            text=fake.paragraph(nb_sentences=9),
        )
    elapsed = datetime.utcnow() - t0
    elapsed = elapsed.total_seconds()
    print(f'total time: {elapsed}')
