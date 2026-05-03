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

