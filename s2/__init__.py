"""SQLAlchemy (core)
"""
from datetime import datetime

from faker import Faker
from memory_profiler import profile

from .models import engine, posts, users

fake = Faker()


@profile
def populate(num_people: int, num_posts: int):
    t0 = datetime.utcnow()
    with engine.begin() as conn:
        for _ in range(num_people):
            user_in = users.insert().values(
                name=fake.name(), active=fake.pybool(),
                joined=fake.past_datetime(start_date='-120d'),
            )
            res = conn.execute(user_in)
            user_pk = res.inserted_primary_key[0]
            values = []
            for _ in range(num_posts):
                values.append({
                    'user_id': user_pk,
                    'title': fake.sentence(),
                    'text': fake.paragraph(nb_sentences=9),
                })
            post_ins = posts.insert().values(values)
            conn.execute(post_ins)
    elapsed = datetime.utcnow() - t0
    elapsed = elapsed.total_seconds()
    print(f'total time: {elapsed}')
