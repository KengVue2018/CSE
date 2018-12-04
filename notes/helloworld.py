'''
print("Hello World")

# This is a comment. This has no effect on the code
# but this does allow me to do things, I can't
# 1. Make notes to myself
# 2. Comment pieces of code that do not work
# 3. Make my code easier to read

print("Look at what happens here. Is there any space?")
print()
print()
print("There should be a couple blank lines here.")
'''
# Math
print(3 + 5)
print(5 - 2)
print(3 + 4)
print(6 / 2)

print("Figure this out...")
print(6 // 2)
print(5 // 2)
print(9 // 4)

print("Here is another one...")
print(6 % 2)
print(5 % 2)
print(11 % 4)  # Modulue (Remainder)

# Powers
# What is 2^100?
print(2 ** 100)

# Taking input
name = input("What is your name?")
print("Hello %s." % name)

age = input("How old are you? >_")
print("%s?!? You belong in a museum." % age)
print()
print("%s is really old. They are %s years old." % (name, age))

# Variable Assignments
car_name = "Wiebe Moblie"
car_type = "GTR"
car_cylinders = 10
car_miles_per_gallon = 0.01

# Make it print "I have a car called "Wiebe Mobile". It is a GTR
print("I have a car called %s. It is a %s." % (car_name, car_type))

# Recasting
real_age = int(input("How old are you again?"))
hidden_age = real_age + 5
print("This is your real age: %d" % hidden_age)

"""
This is a multi-line commwnt 
Anything between the "s is not run.
"""


# Functions
def say_it():
    print("Hello World")


say_it()
say_it()
say_it()


# f(x) = 2x + 3
def f(x):
    print(2*x + 3)


f(1)
f(5)
f(5000)


# Distance Formula
def distance(x1, y1, x2, y2):
     dist = ((x1-x2)**2 + (y2-y1)**2)**(1/2)
     print(dist)


distance(0, 0, 3, 4)
distance(0, 0, 5, 12)

# Loope
for i in range(10000):   # This gives the number 0 through 4
    say_it()

for i in range(1000000):
    print(1 + 1)

for i in range(5):
    f(i)

# While Loops
a = 0
while a < 10:
    print(a)
    a += 1 # This is the same as saying a = a + 1


"""
At the moment you START the loop:
For loops - Use when you know EXACTLY how many literations 
While loops - Use when you DON'T know how many literations
"""

# Control structures (If statement)
sunny = False
if sunny:
    print("Go Outside")


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


your_grade = grade_calc(82)
print(your_grade)


# "Random" Notes
import random  # This should be on line 1
print(random, randint(0, 100))


# Equality Statements
print(5 > 3)
print(5 >= 3)
print(3 == 3)
print(3 != 4)
"""
a = 3  # A is set to 3 
a == 3  # Is a equal to 3?
"""


