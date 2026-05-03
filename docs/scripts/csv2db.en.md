# csv2db

## Required modules

 - csv     -> included in the standard Python installation
 - sqlite3 -> included in the standard Python installation

## Create a sample CSV file

Download: [csv_write_module.py](../examples/basics/csv_write_module.py)

## Script 

The script reads a CSV file containing share data and writes or updates these records in an SQLite database table named `shares`; It then outputs the number of rows imported.

```python
import csv
import sqlite3

csv_file = ‘example_shares.csv’
db_file = ‘example_shares_csv.db’
counter=0

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS shares (
title TEXT primary key,
swx TEXT,
price REAL,
dividend REAL,
volume INTEGER,
monthly_income FLOAT
)
""")

with open(csv_file, mode="r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file, delimiter=“;”)

    for row in reader:
        counter+=1
        cursor.execute("""
        REPLACE INTO shares (title, swx, price, dividend, volume, monthly_income)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            row[‘Title’],
            row[‘SWX’],
            float(row[‘Price’]),
            float(row[‘Dividend’]),
            int(row[‘Volume’]),
            float(row[‘Monthly income’])
        ))

conn.commit()
conn.close()

print(f‘{counter} records have been written into the database’)
```

Download: Download: [csv2db.py](../examples/scripts/csv2db.py)

- It connects to an SQLite database file example_shares_csv.db and, if necessary, creates the table shares with the appropriate columns.
- It opens the CSV file example_shares.csv, reads each row as a dictionary (separated by ;), and converts the values to the appropriate types (float, int).
- For each row, it executes a REPLACE INTO, i.e. existing records with the same title are overwritten, and new ones are inserted.
- Finally, the commit is executed, the connection is closed, and the number of records written is printed.

