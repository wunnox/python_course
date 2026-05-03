# cvs2db

## Required modules

 - csv     -> included in the standard Python installation
 - sqlite3 -> included in the standard Python installation

## Script

The script exports all records from the SQLite table `shares` to a new CSV file `example_shares_new.csv`, writing a header row first, followed by the data rows.

```python
import sqlite3
import csv

db_file = ‘example_shares_csv.db’
csv_file = ‘example_shares_new.csv’

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

cursor.execute(‘SELECT title, swx, price, dividend, volume, monthly_income FROM shares’)
data = cursor.fetchall()

with open(csv_file, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file, delimiter=“;”)

    writer.writerow([‘Title’, ‘SWX’, ‘Price’, ‘Dividend’, “Volume”, ‘Monthly income’])
    writer.writerows(data)

conn.close()

print(f‘Records have been written to {csv_file}’)
```

Download: Download: [db2csv.py](../examples/scripts/db2csv.py)

- It connects to the database `example_shares_csv.db` and reads all columns title, swx, price, dividend, volume, monthly_income from the table shares into the variable `data`.
- It opens the target file `example_shares_new.csv` for writing, creates a CSV writer with ‘;’ as the delimiter, writes a header row with the column names, and then writes all records from `data` to the CSV file.
