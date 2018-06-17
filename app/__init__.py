from CassandraDB import CassandraDB
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from app.models.match import Match
from app.scrapper import scrap

nodes = ['127.0.0.1']
# export CQLENG_ALLOW_SCHEMA_MANAGEMENT="CQLENG_ALLOW_SCHEMA_MANAGEMENT"

print("Connecting to Cassandra DB...")
db = CassandraDB()
session = db.connect()
print("Connection success to Cassandra DB.")

print("Synchronizing Database with Models...")
connection.setup(nodes, "cqlengine", protocol_version=3)
sync_table(Match)
print("Synchronizing Completed...")

print("App started!")

print("Starting scraping...")
scrap()
print("Starting finiched...")
