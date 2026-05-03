# excel2db

## Required modules

 - openpyxl -> external module, must be downloaded from pypi.org
 - sqlite3 -> included in the standard Python installation

## Create an Excel sample file

Download: [module_openpyxl_write.py](../examples/modules/module_openpyxl_write.py)

## Script

The script reads `data` from the Excel file `example_shares.xlsx` and imports it into an SQLite database `example_shares_excel.db` into the table `shares`.

```python
import sqlite3
from openpyxl import load_workbook

excel_file = 'example_shares.xlsx'
db_file = 'example_shares_excel.db'
counter=0

connection = sqlite3.connect(db_file)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS shares (
    title TEXT primary key,
    swx TEXT,
    price REAL,
    dividend REAL,
    volume INTEGER,
    monthly_income TEXT
)
""")

# We want the formula, not just the value, hence data_only=False
workbook = load_workbook(excel_file, data_only=False)
sheet = workbook.active

for row in sheet.iter_rows(min_row=2, values_only=True):
    title, swx, price, dividend, volume, monthly_income = row

    # We don't want the header row
    if title=='Title':
        continue

    counter+=1
    cursor.execute("""
    REPLACE INTO shares (title, swx, price, dividend, volume, monthly_income)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        title,
        swx,
        float(price),
        float(dividend),
        int(volume),
        monthly_income
    ))

connection.commit()
connection.close()

print(f'{counter} records have been written into the database')
```

Download: Download: [excel2db.py](../examples/scripts/excel2db.py)

- It creates (if necessary) the table `shares` with the columns title, swx, price, dividend, volume and monthly_income, linking to the database file.
- It loads the Excel file using `openpyxl`, takes the active worksheet and iterates from row 2 through all row values (values_only=True).
- For each row, the values are assigned to variables, the header is skipped for safety, the numeric fields are converted to float or int, and written to the table using REPLACE INTO (existing rows with the same `title` are overwritten).
- Finally, the changes are saved with `commit`, the connection is closed, and the number of records written is displayed.
