import random
r = random.randint(0, 10)
guesses_left = 5
playing = True

print("Type a number 1-10")

while guesses_left > 0 and playing:
    guess = int(input("Guess="))
    if guess > r:
        print("Lower")
        guesses_left -= 1
    elif guess < r:
        print("Greater")
        guesses_left -= 1
    else:
        print("Corrent!")
        playing = False









