import sqlite3

# Create connection
connection = sqlite3.connect("people.db")
cursor = connection.cursor()

# Insert into table
cursor.execute("INSERT OR IGNORE INTO person values (Null, 'John', 'Doe', 'London')")

# Insert into table
cursor.execute('INSERT OR IGNORE INTO person values (?,?,?,?)',
    (None, "Anna", "Doe", "St. John's"))

# Insert into table
cursor.execute("INSERT OR REPLACE INTO person values (?,?,?,?)",
    (3, 'Fred', 'Doe', 'Leeds'))

# Save to disk
connection.commit()

# Close database
connection.close()
