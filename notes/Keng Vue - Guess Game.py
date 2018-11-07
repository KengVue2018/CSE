import random
random.randint(0, 10)
guesses_left = 5
playing = True
while guesses_left > 0 and playing:
    print("You have %d guesses left" % guesses_left)
    current_guess = int(input("Type in a number between 1 and 10"))
    if current_guess == number:
        print("YOU WIN!!!!!! HUZZAH!!!!")
        playing = False



