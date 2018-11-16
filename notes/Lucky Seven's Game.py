import random
amount_money = 15
rounds = 0

print("You have $15 left")

while amount_money > 0:
    print()
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    print("You got an %s" % str(d1 + d2))
    if d1 + d2 == 7:
        amount_money += 4
        print("You win!")
    else:
        amount_money -= 1
        print("You lose!")
    print("You have $%d left." % amount_money)

a = amount_money
b = rounds














