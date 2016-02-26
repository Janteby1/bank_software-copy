import sqlite3

db = 'bank.db'

users =[
    ["test", "test", "test", 1],
    ["abe", "aanteby", "aanteby", 1],
    ["jack", "janteby", "password", 1],
    ["hymie", "hymieanteby", "password", 1],
    ["banker", "bankerguy", "password", None],
]

acts = [
    ["checking", 1000, 1],
    ["checking", 500, 2],
    ["savings", 1800, 2],
    ["savings", 20000, 3],
    ["checking", 100000, 4],
    ["credit card", 200, 2],
    ["savings", 200, 1],
    ["loan", 600, 4]
]

conn = sqlite3.connect(db)
c = conn.cursor()


for user in users:
    c.execute("""
        INSERT INTO users ("name", "username", "password", "permission") VALUES (?, ?, ?, ?)""",(user[0], user[1], user[2], user[3]))

conn.commit()

for act in acts:
    c.execute("""
        INSERT INTO acts ("acttype", "balance", "userid") VALUES (?, ?, ?)""",(act[0], act[1], act[2]))

conn.commit()

print ("All data loaded")
c.close()


'''
tested - 
sqlite> select name from users where id =(select id from acts where actnum =101);
jack
'''