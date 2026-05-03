# Processing CSV files

## Creating CSV files

A CSV file is very easy to create. Ultimately, it consists solely of text components separated by a delimiter.
A simple example might look like this:

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

The same example using the CSV module:

```python
import csv

data = [
    [‘Title’, ‘SWX’, ‘Price’, ‘Dividend’, “Volume”, ‘Monthly income’],
    [‘Nestle’, ‘NESN’, “79”, ‘3.12’, ‘200’, ‘0.66’],
    [‘UBS’, ‘UBSG’, ‘34’, ‘0.84’, “300”, ‘0.62’],
    [‘SwissRE’, ‘SREN’, “125”, ‘6.28’, ‘400’, ‘1.67’],
]

with open(‘example_shares.csv’, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerows(data)
```

Download: [csv_write_module.py](../examples/basics/csv_write_module.py)

## Reading CSV files

The following example demonstrates how to read a CSV file

```python
import csv

with open(“example_shares.csv”, mode=“r”, encoding="utf-8-sig") as csvfile:
    fields = [“Title”, “SWX”, “Price”, “Dividend”, “Volume”, “Monthly income”]
    reader = csv.DictReader(csvfile,
        fieldnames=fields,
        delimiter=“;”,
        quotechar=“"”,
    )

    #print(reader.fieldnames) # In case the header is not included in the data
    for data in reader:
       print(data[“Title”],data[“SWX”],data[“Price”],data[“Dividend”],data[“Volume”],data[“Monthly income”])
```

Explanations:

- mode=“r” : is the default setting and therefore optional
- encoding="utf-8-sig" : Removes the first character in the case of a BOM signature; does not cause any issues if there is no BOM.
