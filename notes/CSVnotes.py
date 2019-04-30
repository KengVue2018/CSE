import csv


def validate(num: str):
    if all_16_digits(num):
        return False
    if divisible_by_2(num) and divisible_by_3(num):
        return True
    return False


def divisible_by_3(num: str):
    first_num = int(num[0])
    if first_num % 3 == 0:
        return True
    return False


def divisible_by_2(num: str):
    first_num = int(num[0])
    if first_num % 2 == 0:
        return True
    return False


def all_16_digits(num: str):
    if len(num) == 16:
        return True
    else:
        print("NOT EVERY NUMBER IS 16 DIGITS!!!")
        return False

#  with open("Book1.csv") as old_csv:
#  with open("MyNewFile.csv", 'w', newline='') as new_csv:
# print("Writing file...    ")
#   reader = csv.reader(old_csv)
#   writer = csv.writer(new_csv)
#   for row in reader:
#   old_number = int(row[0])
#   new_number = old_number + 1
# row[0] = new_number
# writer.writerow(row)
# print(int(old_number) + 1)
# print(old-number
# print("OK")


with open("Book1.csv") as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...    ")

        for row in reader:
            # old_number = int(row[0]) + 1
            old_number = row[0]  # This is a string # This is the first number
            if validate(old_number):
                writer.writerow(row)
            # print(int(old_number) + 1)
            # print(old-number
print("DONE")


string = input(">_")


def valid_card_number(num: str):
    print(string[:-1])
    print(reverse_it(string))


print(valid_card_number(string))


"""
list_num = list(number)
for index in range(len(list_num)):
    list_num[index] = int(list_num(index))
"""