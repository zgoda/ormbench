Python ORM memory benchmark
===========================

Memory utilization benchmark of 4 ORM libraries:

* Peewee
* Pony ORM
* SQLAlchemy (declarative)
* SQLAlchemy (core)

This benchmark is not fucused on speed - all contenders are quite performant
(Pony is known to be the fastest), but it's putting memory utilization first.

Test 1: insert multiple
-----------------------

Insert 120 User objects and for each User object insert 60 related objects
(Post).
