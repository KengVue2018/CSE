import random
r = random.randint(0, 10)
guesses_left = 5
playing = True

print("Type in a number 1-10")

while guesses_left > 0 and playing:
    guess = input("guesses=")

if guess > r:
        print("Lower")
        guess -= 1
elif guess < r:
        print("Greater")
        guess -= 1
else:
        print("Corrent!")
        playing = False









