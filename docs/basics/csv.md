# CSV-Dateien verarbeiten

## CSV-Dateien erstellen

Eine CSV-Datei kann ganz einfach erstellt werden. Letztendlich sind es nur Textkomponenten, welche mit einem Trennzeichen separiert sind.
Ein einaches Beispiel kann so aussehen:

```python
data=['"Title";"SWX";"Price";"Dividend";"Volume";"Monthly income"\n',
'"Nestle";"NESN";"79";"3.12";"200";"0.66"\n',
'"UBS";"UBSG";"34";"0.84";"300";"0.62"\n',
'"SwissRE";"SREN";"125";"6.28";"400";"1.67"\n'
]

# Write data into a file
with open("example_shares.csv", 'w') as d:
   for line in data:
       d.write(line)
```

Download: [csv_write_simple.py](../examples/basics/csv_write_simple.py)

Dasselbe Beispiel mit dem CSV Modul:

```python
import csv

data = [
    ["Title", "SWX", "Price", "Dividend", "Volume", "Monthly income"],
    ["Nestle", "NESN", "79", "3.12", "200", "0.66"],
    ["UBS", "UBSG", "34", "0.84", "300", "0.62"],
    ["SwissRE", "SREN", "125", "6.28", "400", "1.67"],
]

with open("example_shares.csv", mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerows(data)
```

Download: [csv_write_module.py](../examples/basics/csv_write_module.py)

## CSV-Dateien einlesen

Mit folgendem Beispiel kann eine CSV-Datei wieder eingelesen werden

```python
import csv

with open('example_shares.csv', mode='r', encoding="utf-8-sig") as csvfile:
    fields = ['Title', 'SWX', 'Price', 'Dividend', 'Volume', 'Monthly income']
    reader = csv.DictReader(csvfile,
        fieldnames=fields,
        delimiter=';',
        quotechar='"',
    )

    #print(reader.fieldnames) # Für den Fall, wenn der Header nicht in den Daten steht
    for data in reader:
       print(data['Title'],data['SWX'],data['Price'],data['Dividend'],data['Volume'],data['Monthly income'])
```

Erklärungen:

- mode='r' : ist die default Einstellung und daher optional
- encoding="utf-8-sig" : Löscht den ersten Charakter bei einer BOM-Signatur, stört nicht, wenn es keine hat.



