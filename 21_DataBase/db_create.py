import sqlite3 as sql

db = sql.connect('data.db')

db.execute("CREATE TABLE IF NOT EXISTS users_tb (id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT)")


db.close()

