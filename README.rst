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
These results have been collected without using
`tracemalloc <https://docs.python.org/3/library/tracemalloc.html>`_. With
tracemalloc enabled the results reported for particular lines would be more
accurate but tracemalloc adds ~10 MiB VM overhead.

"Mem usage" column in 1st row shows initial memory allocation for code running
in VM, this includes memory profiler (which is the same in every case) and ORM
connectivity engine allocation.

Results below are based on my desktop machine which is AMD Ryzen 5 3400G,
SATA SSD, 32 GB RAM running Ubuntu Linux 18.04.

Test 1: batch insert
--------------------

Insert 120 ``User`` objects and for each ``User`` object insert 60 related
objects (``Post``).

This test uses all available batch loading techniques for particular library
without resorting to raw SQL and operating on domain objects if possible
(SQLA-core operates at expression level). No library-specific optimizations
are made, only generic Python code structure optimizations.

Results
^^^^^^^

Memory utilization varied from 29.0 MiB (Peewee) to 59.3 MiB (SQLAlchemy ORM),
with SQLA-core (38.9 MiB) and Pony (42.6 MiB) in the middle.

Execution time varied from 38.6 seconds (SQLAlchemy core) to 48.6 seconds
(SQLAlchemy ORM), with Peewee almost catching SQLA-ORM and Pony being in the
middle.

Test 2: insert single object
----------------------------

Insert single ``User`` object, using autocommit if possible.

Results
^^^^^^^

Memory utilization varied from 26.5 MiB (Peewee) to 36.5 MiB (SQLAlchemy ORM),
with Pony (29.8 MiB) and SQLAlchemy Core (31.8 MiB) in the middle.

Execution time was below 0.01 sec except SQLAlchemy ORM where it topped at
0.03 sec.

The difference in memory consumption is still visible, although not that
prominent.

Test 3: insert object with related
----------------------------------

Insert single ``User`` object with related ``Post`` object in one transaction.

Results
^^^^^^^

Memory utilization was almost identical as in Test 2 (26.6, 29.9, 31.9, 36.7
MiB).

Execution time was below 0.02 sec again except for SQLAlchemy ORM which topped
at 0.04 sec.
