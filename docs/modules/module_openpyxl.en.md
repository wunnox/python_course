# Module openpyxl

`openpyxl` is a Python module that allows you to read, write and modify Excel files in the modern XLSX/XLSM format.

Typical uses:

- Creating new workbooks and worksheets, e.g. for automatically generated Excel reports.
- Reading and modifying cell values, formulas and table structures in existing Excel files.
- Applying formatting (fonts, colours, borders) and creating charts directly from Python.

## Example of creating an Excel file

```python
from openpyxl import Workbook

# Your sample data
data = [
    ['Title', 'SWX', 'Price', 'Dividend', 'Volume', 'Monthly income'],
    ['Nestle', 'NESN', '79', '3.12', '200', '0.66'],
    ['UBS', 'UBSG', '34', '0.84', '300', '0.62'],
    ['SwissRE', 'SREN', '125', '6.28', '400', '1.67'],
]

# Create a new workbook
wb = Workbook()
ws = wb.active
ws.title = 'Shares'

# Write rows to the worksheet
for row in data:
    ws.append(row)

# Save the file
excel_file = 'example_shares.xlsx'
wb.save (excel_file)

print(f'Excel file saved as {excel_file}')
```

Download: [module_openpyxl_write.py](../examples/modules/module_openpyxl_write.py)

This script creates a new workbook, renames the active worksheet to “Shares”, appends each row from `data` as a row, and then saves it as `example_shares.xlsx`.

## Example of reading an Excel file

```python
from openpyxl import load_workbook

excel_file = 'example_shares.xlsx'

# Load the workbook
wb = load_workbook(excel_file)
ws = wb.active   # or: wb['Shares'], if named as such

# First row is the header
headers = [cell.value for cell in ws[1]]
print('Header:', headers)

# Read data rows from row 2 onwards
data = []
for row in ws.iter_rows(min_row=2, values_only=True):
    data.append(row)

# Output the read data
for row in data:
    print(row)
```

Download: [module_openpyxl_read.py](../examples/modules/module_openpyxl_read.py)

The script loads the Excel file, reads the header row separately, and then iterates over all data rows from row 2 onwards, outputting each row as a tuple.
