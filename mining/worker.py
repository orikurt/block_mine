from pyArango.connection import *
from pyArango.theExceptions import *
from celery import Celery
from models import *

conn = Connection(username="root", password="")
try:
    conn.createDatabase(name="blockchain")
except CreationError:
    pass
db = conn["blockchain"]
try:
    blocks = db.createCollection("Blocks")
except CreationError:
    pass
try:
    addresses = db.createCollection("Addresses")
except CreationError:
    pass
try:
    transactions = db.createCollection("Transaction")
except CreationError:
    pass
try:
    blockchain = db.createGraph("Blockchain")
except CreationError:
    pass
print("DB: {0}".format(db))

app = Celery("blockchain")
app.conf.broker_url = "redis://localhost:6379/10"

@app.task
def save_block(block):
    pass

if __name__=="__main__":
    app.worker_main()