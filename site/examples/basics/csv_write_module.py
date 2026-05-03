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
