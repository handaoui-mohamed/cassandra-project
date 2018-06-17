from cassandra.cluster import Cluster

KEYSPACE = "cassandra_project"


class CassandraDB:

    def connect(self, nodes=[]):
        cluster = Cluster()
        session = cluster.connect(nodes)
        session.execute("DROP keyspace IF EXISTS %s" % KEYSPACE)
        session.execute(
            """
            CREATE KEYSPACE IF NOT EXISTS %s WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor': 1};
            """ % KEYSPACE
        )
        session = cluster.connect(keyspace=KEYSPACE)
        return session
