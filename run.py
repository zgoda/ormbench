from argparse import ArgumentParser, Namespace
from importlib import import_module


def get_options() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument('module', choices=['peewee', 'pony', 'sqla', 'all'])
    opts = parser.parse_args()
    return opts


def run_profile(mod_name: str):
    module = import_module(mod_name)
    module.populate(120, 60)
    module.clean()


def main():
    module_name_map = {
        'peewee': 'p1',
        'pony': 'p2',
        'sqla': 's1',
    }
    opts = get_options()
    if opts.module == 'all':
        pass
    else:
        run_profile(module_name_map[opts.module])


if __name__ == '__main__':
    main()
