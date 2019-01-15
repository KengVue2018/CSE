import random
import string
word_list = ["ANIME", "THAILAND", "SLAYER", "DIAMONDS", "ANYTHING", "GOOD", "SUPERMAN", "DRAGON", "BREAK", "SPIDERMAN"]
list_of_letters = string.ascii_letters

turns = 8

output = []
word_selection = random.choice(word_list)
length = len(word_selection)
for i in range(length):
    output.append("_ ")
print("".join(output))
print(word_selection)

dashes = "_" * len(word_selection)

while turns > -1 and not dashes == word_selection:
    print(dashes)
    print(str(turns))
    turns = input("turns:")
    if len(turns) !=1:
        print("Your guess must have exactly one character")
    elif turns in word_selection:
        print("That letter is in the secret word!")
        dashes = update_dashes(word_selection, dashes, turns)

























