# excel2db

## Benötigte Module

 - openpyxl -> externes Modul, muss von pypi.org geladen werden
 - sqlite3 -> in der standard Python-Installation enthalten

## Excel Beispieldatei erstellen

Download: [module_openpyxl_write.py](../examples/modules/module_openpyxl_write.py)

## Script 

Das Skript liest Daten aus der Excel-Datei `example_shares.xlsx` ein und importiert sie in eine SQLite-Datenbank `example_shares_excel.db` in die Tabelle `shares`.

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

# We want the formula not just the value, hence data_only=False
workbook = load_workbook(excel_file, data_only=False)
sheet = workbook.active

for row in sheet.iter_rows(min_row=2, values_only=True):
    title, swx, price, dividend, volume, monthly_income = row

    # We don't want the header line
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

print(f"{counter} records have been written into the database")
```

Download: Download: [excel2db.py](../examples/scripts/excel2db.py)

- Es erstellt (falls nötig) die Tabelle `shares` mit den Spalten title, swx, price, dividend, volumeund monthly_income Verknüpfung mit der Datenbankdatei.
- Es lädt die Excel-Datei mit `openpyxl`, nimmt das aktive Tabellenblatt und iteriert ab Zeile 2 über alle Zeilenwerte ( values_only=True).
- Für jede Zeile werden die Werte auf Variablen verteilt, der Header zur Sicherheit übersprungen, die numerischen Felder in float bzw. int umgewandelt und per REPLACE INTOin die Tabelle geschrieben (vorhandene Zeilen mit demselben `title` werden überschrieben).
- Am Ende werden die Änderungen mit `commit` gespeichert, die Verbindung geschlossen und ausgegeben, wie viele Datensätze geschrieben wurden.



