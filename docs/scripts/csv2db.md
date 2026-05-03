# cvs2db

## Benötigte Module

 - csv     -> in der standard Python-Installation enthalten
 - sqlite3 -> in der standard Python-Installation enthalten

## CSV Beispieldatei erstellen

Download: [csv_write_module.py](../examples/basics/csv_write_module.py)

## Script 

Das Script liest eine CSV-Datei mit Aktien-Daten ein und schreibt bzw. aktualisiert diese Datensätze in einer SQLite-Datenbank-Tabelle namens shares; Danach gibt es aus, wie viele Zeilen importiert wurden.

```python
import csv
import sqlite3

csv_file = "example_shares.csv"
db_file = "example_shares_csv.db"
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
    reader = csv.DictReader(file, delimiter=';')

    for row in reader:
        counter+=1
        cursor.execute("""
        REPLACE INTO shares (title, swx, price, dividend, volume, monthly_income)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            row["Title"],
            row["SWX"],
            float(row["Price"]),
            float(row["Dividend"]),
            int(row["Volume"]),
            float(row["Monthly income"])
        ))

conn.commit()
conn.close()

print(f"{counter} records have been written into the database")
```

Download: Download: [csv2db.py](../examples/scripts/csv2db.py)

- Es stellt eine Verbindung zu einer SQLite-Datenbankdatei example_shares_csv.dbher und legt bei Bedarf die Tabelle sharesmit den passenden Spalten an.
- Es öffnet die CSV-Datei example_shares.csv, liest jede Zeile als Dict (Trennzeichen ;) und wandelt die Werte in passende Typen (float, int) um.
- Für jede Zeile führt es ein REPLACE INTOaus, d. H. Bestehende Datensätze mit demselben titlewerden überschrieben, neue werden eingefügt.
- Am Ende wird der Commit ausgeführt, die Verbindung geschlossen und die Anzahl der geschriebenen Datensätze mit printausgegeben.


