from argparse import ArgumentParser, Namespace
from importlib import import_module


def get_options() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        'module', choices=['peewee', 'pony', 'sqla-orm', 'sqla-core']
    )
    opts = parser.parse_args()
    return opts


def run_profile(mod_name: str):
    module = import_module(mod_name)
    try:
        module.populate(120, 60)
    finally:
        module.clean()


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
