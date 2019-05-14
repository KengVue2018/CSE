import csv

with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    for row in reader:
        if row[0] == 'Region':
            continue
            # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == 'Fruits':
            total += float(old_number)
            # print(old_number)


total = round(total, 2)
print("The total fruits profit was:")
print("${:,}".format(total))


with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    for row in reader:
        if row[0] == 'Region':
            continue
            # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == 'Clothes':
            total += float(old_number)
            # print(old_number)


total = round(total, 2)
print("------")
print("The total clothes profit was:")
print("${:,}".format(total))


with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    for row in reader:
        if row[0] == 'Region':
            continue
            # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == 'Meat':
            total += float(old_number)
            # print(old_number)


total = round(total, 2)
print("------")
print("The total MeaT profit was:")
print("${:,}".format(total))


with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    for row in reader:
        if row[0] == 'Region':
            continue
            # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == 'Beverages':
            total += float(old_number)
            # print(old_number)


total = round(total, 2)
print("------")
print("The total Beverages profit was:")
print("${:,}".format(total))


with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    for row in reader:
        if row[0] == 'Region':
            continue
            # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == 'Office Supplies':
            total += float(old_number)
            # print(old_number)


total = round(total, 2)
print("------")
print("The total Office Supplies profit was:")
print("${:,}".format(total))


with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    for row in reader:
        if row[0] == 'Region':
            continue
            # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == 'Cosmetics':
            total += float(old_number)
            # print(old_number)


total = round(total, 2)
print("------")
print("The total Cosmetics profit was:")
print("${:,}".format(total))


with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    for row in reader:
        if row[0] == 'Region':
            continue
            # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == 'Snacks':
            total += float(old_number)
            # print(old_number)


total = round(total, 2)
print("------")
print("The total Snacks profit was:")
print("${:,}".format(total))


with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    for row in reader:
        if row[0] == 'Region':
            continue
            # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == 'Personal Care':
            total += float(old_number)
            # print(old_number)


total = round(total, 2)
print("------")
print("The total Personal Care profit was:")
print("${:,}".format(total))


with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    for row in reader:
        if row[0] == 'Region':
            continue
            # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == 'Household':
            total += float(old_number)
            # print(old_number)


total = round(total, 2)
print("------")
print("The total Household profit was:")
print("${:,}".format(total))


with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    for row in reader:
        if row[0] == 'Region':
            continue
            # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == 'Vegetables':
            total += float(old_number)
            # print(old_number)


total = round(total, 2)
print("------")
print("The total Vegetables profit was:")
print("${:,}".format(total))

with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    for row in reader:
        if row[0] == 'Region':
            continue
            # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == 'Baby Food':
            total += float(old_number)
            # print(old_number)


total = round(total, 2)
print("------")
print("The total Baby Food profit was:")
print("${:,}".format(total))


with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    for row in reader:
        if row[0] == 'Region':
            continue
            # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == 'Cereal':
            total += float(old_number)
            # print(old_number)


total = round(total, 2)
print("------")
print("The total Cereal profit was:")
print("${:,}".format(total))


with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    for row in reader:
        if row[0] == 'Region':
            continue
            # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == 'Cosmetics':
            total += float(old_number)
            # print(old_number)


total = round(total, 2)
print("------")
print("------")
print("Cosmetics is the most profited item.")
print("${:,}".format(total))
