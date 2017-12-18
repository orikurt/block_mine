from pyArango.connection import *

conn = Connection(username="root", password="")
db = conn.createDatabase(name="blockchain")

print(db)

