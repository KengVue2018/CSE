import random
money = int(input("You have $15"))
rolldice1 = random.randint(1, 6)
rolldice2 = random.randint(1, 6)
role = (rolldice1 + rolldice2)
while True:
    if role == 7:
        print("Nice your roll was a 7, you get to roll again: ", money + 4)











