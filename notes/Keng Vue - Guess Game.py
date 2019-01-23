import random
r = random.randint(0, 10)
guesses_left = 5
playing = True

print("Type in a number 1-10")

while guesses_left > 0 and playing:
    guesses_left = int(input("guesses="))

if guesses_left > r:
        print("Lower")
        guesses_left -= 1
elif guesses_left < r:
        print("Greater")
        guesses_left -= 1
else:
        print("Corrent!")
        playing = False









