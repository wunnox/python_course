# db2excel

## Required modules

 - openpyxl -> external module, must be downloaded from pypi.org
 - sqlite3 -> included in the standard Python installation

## Script

The script reads data from the SQLite database `example_shares_excel.db` and writes it to a new Excel file `example_shares_new.xlsx`.

```python
import sqlite3
from openpyxl import Workbook

db_file = 'example_shares_excel.db'
excel_file = 'example_shares_new.xlsx'

connection = sqlite3.connect(db_file)
cursor = connection.cursor()

cursor.execute("SELECT title, swx, price, dividend, volume, monthly_income FROM shares")
data = cursor.fetchall()

workbook = Workbook()
sheet = workbook.active
sheet.title = 'Shares'

sheet.append(['Title', 'SWX', 'Price', 'Dividend', 'Volume', 'Monthly income'])

for row in data:
    sheet.append(row)

workbook.save(excel_file)

connection.close()

print(f'Records have been written to {excel_file}')
``` 

Download: [db2excel.py](../examples/scripts/db2excel.py)

- It connects to the database, executes a `SELECT` on the `shares` table and retrieves all records into `data`.
- It creates a new workbook using `openpyxl`, renames the active sheet to “Shares” and first writes a header row with the column names.
- It then appends each row from `data` as a new row in the spreadsheet, saves the workbook as `example_shares_new.xlsx`, closes the DB connection and outputs a success message.
