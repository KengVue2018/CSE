import random
import string
word_list = ["GAREN", "THAILAND", "SLAYER", "DIAMONDS", "MASTER YI", "ZED", "SUPERMAN", "DRAGON", "BREAK", "YASUO"]
list_of_letters = string.ascii_letters

turns = 8

letters_guessed = []
word_selection = random.choice(word_list)
length = len(word_selection)
for i in range(length):
    letters_guessed.append("_ ")
print("".join(letters_guessed))
print(word_selection)

playing = True

while turns > 0 and playing:
    hidden_word = []
    for letter in word_selection:
        if letter in letters_guessed:
            hidden_word.append(letter)

        else:
            hidden_word.append("")
            print("".join(hidden_word))

            user_guess = input("Guess a letter:")
            print('\n * 10')
            if user_guess.lower() in word_selection or user_guess.upper() in word_selection:
                print("You got it right")
                for i in range(len(word_selection)):
                    if word_selection[i].lower() == user_guess.lower():
                        letters_guessed.pop(i)