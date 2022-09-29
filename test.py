import sqlite3

db = sqlite3.connect('Library.db')
cursor = db.execute("SELECT Member_ID from First_Table")
for row in cursor.fetchall():
    h = str(row)
    print(h)