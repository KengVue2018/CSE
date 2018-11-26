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
