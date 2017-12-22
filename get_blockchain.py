from pyArango.connection import *
from pyArango.theExceptions import *

conn = Connection(username="root", password="")
try:
    conn.createDatabase(name="blockchain")
except CreationError:
    pass
db = conn["blockchain"]
print(db)

