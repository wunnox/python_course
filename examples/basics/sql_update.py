import sqlite3

# Create connection
connection = sqlite3.connect("people.db")
cursor = connection.cursor()

# Update table
cursor.execute("UPDATE person SET city='Glasgow' WHERE id=1")

# Update table
cursor.execute('UPDATE person SET city=? WHERE id=?', ('Brighton',2))

# Update table
id=3
city='Birmingham'
cursor.execute(f"UPDATE person SET city='{city}' WHERE id={id}")

# Save to disk
connection.commit()

# Close database
connection.close()
