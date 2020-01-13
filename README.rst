Python ORM memory benchmark
===========================

Memory utilization benchmark of 4 ORM libraries:

* `Peewee <http://docs.peewee-orm.com/>`_
* `Pony ORM <https://docs.ponyorm.org/>`_
* `SQLAlchemy (declarative) <https://docs.sqlalchemy.org/en/13/orm/tutorial.html>`_
* `SQLAlchemy (core) <https://docs.sqlalchemy.org/en/13/core/tutorial.html>`_

This benchmark is not fucused on speed - all contenders are quite performant
(Pony is known to be the fastest, Peewee has the smallest memory footprint,
etc), but it's putting memory utilization first. There's already interesting
`Python ORM benchmark <https://github.com/tortoise/orm-benchmarks>`_ that is
mostly speed aligned.

Memory usage is measured with
`memory-profiler <https://pypi.org/project/memory-profiler/>`_ library with
SQLite as database backend.

The numbers one may actually get will differ but they should still be valid
for comparisons as long as the test runs are performed in the same conditions.

Results below are based on my desktop machine which is AMD Ryzen 5 3400G,
SATA-II SSD, 32 GB RAM running Ubuntu Linux 18.04.

Test 1: insert multiple
-----------------------

Insert 120 ``User`` objects and for each ``User`` object insert 60 related
objects (``Post``).

This test uses all available bulk loading techniques for particular library
without resorting to raw SQL and operating on domain objects if possible
(SQLA-core operates at expression level).

Results
^^^^^^^

Memory utilization varied from 29.0 MiB (Peewee) to 59.3 MiB (SQLAlchemy ORM),
with SQLA-core (38.5 MiB) and Pony (42.6 MiB) in the middle.

Execution time varied from 38.7 seconds (SQLAlchemy core) to 48.6 seconds
(SQLAlchemy ORM), with Peewee almost catching SQLA-ORM and Pony being in the
middle.
