import os

from argparse import ArgumentParser, Namespace
from importlib import import_module


def get_options() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        'module', choices=['peewee', 'pony', 'sqla-orm', 'sqla-core']
    )
    opts = parser.parse_args()
    return opts


def clean(mod_name: str):
    db_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), mod_name, 'db.sqlite')
    )
    os.unlink(db_path)


def run_profile(mod_name: str):
    module = import_module(mod_name)
    try:
        module.populate(120, 60)
    finally:
        clean(mod_name)


def main():
    module_name_map = {
        'peewee': 'p1',
        'pony': 'p2',
        'sqla-orm': 's1',
        'sqla-core': 's2',

    }
    opts = get_options()
    run_profile(module_name_map[opts.module])


if __name__ == '__main__':
    main()
