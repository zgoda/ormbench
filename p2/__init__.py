import os

DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'db.sqlite'))
os.environ['DB_PATH'] = DB_PATH

from faker import Faker
from memory_profiler import profile
from pony.orm import db_session

from .models import Post, User

fake = Faker()


@profile
@db_session
def populate(num_people: int, num_posts: int):
    for _ in range(num_people):
        user = User(
            name=fake.name(), active=fake.pybool(),
            joined=fake.past_datetime(start_date='-120d'),
        )
        for _ in range(num_posts):
            Post(user=user, title=fake.sentence(), text=fake.paragraph(nb_sentences=9))


def clean():
    os.unlink(DB_PATH)
