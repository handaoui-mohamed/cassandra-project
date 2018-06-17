from cassandra.cqlengine.models import Model
from CassandraDB import KEYSPACE


class Base(Model):
    __abstract__ = True
    __keyspace__ = KEYSPACE
