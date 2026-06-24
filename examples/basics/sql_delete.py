import sqlite3

# Create connection
connection = sqlite3.connect("people.db")
cursor = connection.cursor()

# Delete record
cursor.execute("DELETE FROM person WHERE id=3")

# Delete record
cursor.execute("DELETE FROM person WHERE id=?",(2,))

# Delete record
id=1
cursor.execute(f"DELETE FROM person WHERE id={id}")

# Save to disk
connection.commit()

# Close database
connection.close()
