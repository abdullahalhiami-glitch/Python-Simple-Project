import sqlite3 as sql 
import os


DB_NAME = os.path.join(os.path.dirname(__file__), "Restaurants.db") 
db=sql.connect(DB_NAME)
cur=db.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS restaurants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    cuisine_type TEXT NOT NULL
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS ratings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    restaurant_id INTEGER NOT NULL,
    rating_value REAL NOT NULL,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants (id) ON DELETE CASCADE
)
''')

db.commit()
db.close()

print("Database and tables created successfully.")
