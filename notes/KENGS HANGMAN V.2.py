import random
import string

guess = 8
pun = list(string.punctuation)
alphabet = string.ascil_letters
word_list = ["GAREN", "THAILAND", "SLAYER", "DIAMONDS", "MASTER YI", "ZED", "SUPERMAN", "DRAGON", "BREAK", "YASUO"]


random = random.choice(word_list)
random_word = list(random)
letters_guessed = []

win = False
for i in range(len(random)):
    if range[i] in alphabet:
        random_word.pop[i]
        random_word.insert(1, "_")
        if random [i] in pun:
            random.insert(i, "!")
            print(''.join(random_word))

while guess > 0 and not win:
    guess1 = input("Guess a letter =")
    print(guess1)
    letters_guessed.append(guess1.lower)
    for i in range(len(random)):
        if random[i].lower():
            random_word.pop(i)
            random_word.insert(i, random_word)
            if guess1.lower() not in random_word and guess.upper() not in random_word:
                guess -= 1
                print("".join(random_word))
                if "_" not in random_word:
                    win = True
                    print("You Win! Congrauation!")

