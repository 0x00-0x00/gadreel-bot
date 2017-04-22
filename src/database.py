from shemutils.database import *

#  Define the database object
db = Database("teleManagerDB")

# Create table architecture
t1 = Table("CONVERSATIONS", {
    1: ('FROM_USER', TEXT),
    2: ('MESSAGE', TEXT),
    3: ('TIMESTAMP', TEXT)
    })
db.controller.execute(t1.create())

t2 = Table("ARQUIVOS", {
    1: ('FROM_USER', TEXT),
    2: ('FILE_ID', TEXT),
    3: ('FILE_NAME', TEXT),
    })
db.controller.execute(t2.create())

t3 = Table("TASKS", {
    1: ('FROM_USER', TEXT),
    2: ('CHAT_ID', TEXT),
    3: ('TASK_ID', TEXT),
    4: ('TASK_NAME', TEXT),
    5: ('STATUS', TEXT),
    6: ('TIMESTAMP', TEXT),
})
db.controller.execute(t3.create())

t4 = Table("MEMBERS", {
    1: ('USER_ID', TEXT),
    2: ('STATUS', TEXT),
    3: ('TIMESTAMP', TEXT)
})
db.controller.execute(t4.create())
db.save()