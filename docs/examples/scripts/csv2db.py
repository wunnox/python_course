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
