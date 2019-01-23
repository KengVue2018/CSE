import random
import string
word_list = ["GAREN", "THAILAND", "SLAYER", "DIAMONDS", "MASTER YI", "ZED", "SUPERMAN", "DRAGON", "BREAK", "YASUO"]
list_of_letters = string.ascii_letters

turns = 8

output = []
word_selection = random.choice(word_list)
length = len(word_selection)
for i in range(length):
    output.append("_ ")
print("".join(output))
print(word_selection)

playing = True

while turns > 0 and playing:
    user_guess = input("Guess a letter:")
    print('\n * 10')
    if user_guess.lower() in word_selection or user_guess.upper() in word_selection:
        print("You got it right")
        for i in range(len(word_selection)):
            if word_selection[i].lower() == user_guess.lower():
                output.pop(i)
                



