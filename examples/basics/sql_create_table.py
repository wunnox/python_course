import sqlite3

# Create connection
connection = sqlite3.connect("people.db")
cursor = connection.cursor()

# Create table
cursor.execute("""CREATE TABLE if not exists person (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT,
    lastname TEXT,
    city TEXT)""")

# Save to disk
connection.commit()

# Close database
connection.close()
