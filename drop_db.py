from CassandraDB import CassandraDB

nodes = ['127.0.0.1']
# export CQLENG_ALLOW_SCHEMA_MANAGEMENT="CQLENG_ALLOW_SCHEMA_MANAGEMENT"

print("Connecting to Cassandra Clusters...")
db = CassandraDB()
print("Connection success.")

print("Dropping Database...")
db.drop()
print("Database Dropped...")
