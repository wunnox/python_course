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
