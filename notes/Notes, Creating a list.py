'''
# creating a list
colors = ["blue", "turquoise", "pink", "black", "red", "orange"]  # USE SQUARE BRACKETS!!!!!
print(colors)
print(colors[1])
print(colors[0])

# Length of the lists
print("There are %d things in the lists." % len(colors))

# Changing Elements in a list
colors[1] = "green"
print(colors)

# looping through lists
for idem in colors:
    print(idem)
'''

'''
# new list
cities = ["Fresno", "San Francisco", "Sacramento", "LA", "Las Vegas", "San Diego", "San Jose"]
cities[3] = "Bakersfield"
print(cities)
print("The last thing in the list is %d" % cities[len(cities) - 1])

# Slicing a list
print(cities[1:3])
print(cities[1:4])
print(cities[1:])
print(cities[:4])
'''


food_list = ["pizza", "tamales", "tacos", "pie", "enchiladas", "burrito", "sushi", "poke", "flan", "noodles", "pork",
             "chicken", "beef", "ice cream", "ham", "turkey", "fish", "cod", "mash potatoes", "bacon", "salad"]
print(len(food_list))

# Adding stuff to a list
food_list.append("bread")
food_list.append("eggs")
# Notice that everything is objective.method(parameters)
print(food_list)

food_list.insert(1, "eggo waffles")
print(food_list)


# Removing things in a list
food_list.remove("salad")
print(food_list)


'''
subjects_list = ["math", "english", "science"]
subjects_list.append("pe")
subjects_list.remove("english")
print(subjects_list)
'''


'''
# Tuples
brands = ("apple", "samsung", "HTC")  # Notice the Parenthesis
'''


# Also removing stuff from a list
print(food_list)
food_list.pop(0)
print(food_list)


# find the index of an idem
print(food_list.index("chicken"))

# Changing things into a list
string1 = "turquoise"
list1 = list(string1)
print(list1)


for i in range(len(list1)):  # 1 goes through all indices
    if list1[1] == "u":  # if we find a U
        list1.pop(1)  # remove the i-th index
        list1.insert(1, "*")  # Put a * there instead

'''
for character in list1:
    if character == "u":
    # replace with a *
    current_index = list1.index(character)
    list1.pop(current_index)
    list1.insert(current_index, "*")
'''

# Turn a list into a string
print("".join(list1))


