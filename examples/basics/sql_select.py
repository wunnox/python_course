import sqlite3

# Create connection
connection = sqlite3.connect("people.db")
cursor = connection.cursor()

# select all records
cursor.execute("SELECT * from person")
for row in cursor:
    print(row[0],row[1],row[2],row[3])

# select only where lastname='Doe'
cursor.execute("SELECT firstname,lastname from person where lastname='Doe'")
names=cursor.fetchall()
for firstname,lastname in names:
    print(firstname,lastname)

# select by id
cursor.execute("SELECT lastname,city from person where id=3")
firstname,lastname=cursor.fetchone()
print(firstname,lastname)

# Close database
connection.close()
