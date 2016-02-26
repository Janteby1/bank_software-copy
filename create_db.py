
import sqlite3

connection = sqlite3.connect('bank.db')
cursor = connection.cursor()

connection.execute(
    """
    DROP TABLE IF EXISTS users;
    """
)
connection.execute(
    """
    DROP TABLE IF EXISTS acts;
    """
)

connection.execute(
    """
    CREATE TABLE users (
        id INTEGER PRIMARY KEY, 
        name TEXT, 
        username TEXT, 
        password TEXT,
        permission INTEGER
    )
    """
)

connection.execute(
    """
    CREATE TABLE acts (
        id INTEGER PRIMARY KEY, 
        acttype TEXT, 
        balance INTEGER, 
        userid INTEGER,
        FOREIGN KEY(userid) REFERENCES users(id)
    )
    """
)

connection.commit()

print ("Database created")
connection.close()

