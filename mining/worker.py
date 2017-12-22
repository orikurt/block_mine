from pyArango.connection import *
from pyArango.theExceptions import *
from celery import Celery

conn = Connection(username="root", password="")
try:
    conn.createDatabase(name="blockchain")
except CreationError:
    pass
db = conn["blockchain"]
print(db)

app = Celery("blocks")
app.conf.broker_url = "redis://localhost:6379/10"

@app.task
def save_block(block):
    pass

if __name__=="__main__":
    app.worker_main()