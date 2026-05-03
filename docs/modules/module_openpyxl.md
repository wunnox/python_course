# Modul openpyxl

`openpyxl` ist ein Python-Modul, mit dem du Excel-Dateien im modernen XLSX-/XLSM-Format lesen, schreiben und verändern kannst.

Typische Einsatzzwecke:

- Erstellen neuer Arbeitsmappen und Tabellenblätter, z. B. für automatisch generierte Excel-Reports.
- Auslesen und Ändern von Zellwerten, Formeln und Tabellenstrukturen in bestehenden Excel-Dateien.
- Anwenden von Formatierungen (Schriftarten, Farben, Rahmen) sowie Erstellen von Diagrammen direkt aus Python heraus.

## Beispiel zum Erstellen einer Excel-Datei

```python
from openpyxl import Workbook

# Deine Beispiel-Daten
data = [
    ['Title', 'SWX', 'Price', 'Dividend', 'Volume', 'Monthly income'],
    ['Nestle', 'NESN', '79', '3.12', '200', '0.66'],
    ['UBS', 'UBSG', '34', '0.84', '300', '0.62'],
    ['SwissRE', 'SREN', '125', '6.28', '400', '1.67'],
]

# Neue Arbeitsmappe erstellen
wb = Workbook()
ws = wb.active
ws.title = 'Shares'

# Zeilen in das Arbeitsblatt schreiben
for row in data:
    ws.append(row)

# Datei speichern
excel_file = 'example_shares.xlsx'
wb.save(excel_file)

print(f'Excel-Datei wurde als {excel_file} gespeichert')
```

Download: [module_openpyxl_write.py](../examples/modules/module_openpyxl_write.py)

In diesem Skript wird eine neue Arbeitsmappe erstellt, das aktive Arbeitsblatt in „Shares“ umbenannt, jede Liste aus `data` als Zeile angehängt und anschließend als `example_shares.xlsx` gespeichert.

## Beispiel zum Einlesen einer Excel-Datei

```python
from openpyxl import load_workbook

excel_file = 'example_shares.xlsx'

# Arbeitsmappe laden
wb = load_workbook(excel_file)
ws = wb.active   # oder: wb['Shares'], falls so benannt

# Erste Zeile ist der Header
headers = [cell.value for cell in ws[1]]
print('Header:', headers)

# Datenzeilen ab Zeile 2 einlesen
data = []
for row in ws.iter_rows(min_row=2, values_only=True):
    data.append(row)

# Ausgabe der eingelesenen Daten
for row in data:
    print(row)
```

Download: [module_openpyxl_read.py](../examples/modules/module_openpyxl_read.py)

Das Skript lädt die Excel-Datei, liest die Kopfzeile separat ein und iteriert dann über alle Datenzeilen ab Zeile 2, wobei jede Zeile als Tupel ausgegeben wird.
