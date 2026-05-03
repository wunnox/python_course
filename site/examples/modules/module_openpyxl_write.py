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
