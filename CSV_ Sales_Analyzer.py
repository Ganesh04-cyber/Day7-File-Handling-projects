import csv

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row["Product"]
        quantity = int(row["Quantity"])
        price = int(row["Price"])
        total = quantity * price
        print(f"{product} -> Total Sale: ₹{total}")
