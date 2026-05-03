# cvs2db

## Benötigte Module

 - csv     -> in der standard Python-Installation enthalten
 - sqlite3 -> in der standard Python-Installation enthalten

## Script 

Das Skript exportiert alle Datensätze aus der SQLite-Tabelle sharesin eine neue CSV-Datei example_shares_new.csvund schreibt dabei zuerst eine Kopfzeile, danach die Datenzeilen.

```python
import sqlite3
import csv

db_file = "example_shares_csv.db"
csv_file = "example_shares_new.csv"

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

cursor.execute("SELECT title, swx, price, dividend, volume, monthly_income FROM shares")
data = cursor.fetchall()

with open(csv_file, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file, delimiter=';')
    
    writer.writerow(["Title", "SWX", "Price", "Dividend", "Volume", "Monthly income"])
    writer.writerows(data)

conn.close()

print(f"Records have been written in to {csv_file}")
```

Download: Download: [db2csv.py](../examples/scripts/db2csv.py)

- Es verbindet sich mit der Datenbank `example_shares_csv.db` und liest alle Spalten title, swx, price, dividend, volume, monthly_incomeaus der Tabelle shares in die Variable `data` ein.
- Es öffnet die Zieldatei `example_shares_new.csv` zum Schreiben, erzeugt einen CSV-Writer mit ";" als Trennzeichen, schreibt eine Header-Zeile mit den Spaltennamen und anschließend alle Datensätze aus `data` in die CSV-Datei.


