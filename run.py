import os

from argparse import ArgumentParser, Namespace
from importlib import import_module


def get_options() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        'module', choices=['peewee', 'pony', 'sqla-orm', 'sqla-core']
    )
    parser.add_argument('-t', '--test', default='all')
    opts = parser.parse_args()
    return opts


def clean(mod_name: str):
    db_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), mod_name, 'db.sqlite')
    )
    os.unlink(db_path)


def run_profile(mod_name: str, test: str):
    module = import_module(mod_name)
    try:
        if test == 'all':
            module.populate(120, 60)
        else:
            test_func = getattr(module, test, None)
            if test_func is None:
                raise RuntimeError(f'{test_func} not available for {mod_name}')
            test_func()
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
    run_profile(module_name_map[opts.module], opts.test)


if __name__ == '__main__':
    main()
