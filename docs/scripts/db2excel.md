# db2excel

## Benötigte Module

 - openpyxl -> externes Modul, muss von pypi.org geladen werden
 - sqlite3 -> in der standard Python-Installation enthalten

## Script 

Das Skript liest Daten aus der SQLite-Datenbank `example_shares_excel.db` und schreibt sie in eine neue Excel-Datei `example_shares_new.xlsx`.

```python
import sqlite3
from openpyxl import Workbook

db_file = 'example_shares_excel.db'
excel_file = 'example_shares_new.xlsx'

connection = sqlite3.connect(db_file)
cursor = connection.cursor()

cursor.execute('SELECT title, swx, price, dividend, volume, monthly_income FROM shares')
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

Download: Download: [db2excel.py](../examples/scripts/db2excel.py)

- Es stellt eine Verbindung zur Datenbank her, führt einen `SELECT` auf die Tabelle sharesaus und holt alle Datensätze in `data`.
- Es wurde mit `openpyxl` einer neuen Arbeitsmappe erstellt, benennt das aktive Blatt in „Shares“ und schreibt zunächst eine Header-Zeile mit den Spaltennamen.
- Danach hängt es jede Zeile aus dataals neue Zeile im Tabellenblatt an, speichert die Arbeitsmappe als `example_shares_new.xlsx`, schließt die DB-Verbindung und gibt eine Erfolgsnachricht aus.
