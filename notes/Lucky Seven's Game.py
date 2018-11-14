import random
amount_money = 15
rounds = 0
playing = True

while amount_money > 0:
    d1 = (random.randint(1, 6))
    d2 = (random.randint(1, 6))

88
if d1 + d2 == 7:
    amount_money += 5
    print("You win!")
    print(amount_money)

if d1 + d2 != 7:
    amount_money -= 1
    print("You lose!")
    print(amount_money)












