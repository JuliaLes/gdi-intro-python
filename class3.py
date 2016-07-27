# GDI Intro Python Class 3
# 7/26/16ystems.com/gdi

# url for slides: bysystems.com/gdi

def bostonize(word):
    return('Wicked ' + word)

# Write a function that a bar could use to check to see if a customer is of drinking age.

def isDrinkingAge(age):
    if age >= 21:
        print("This customer is of drinking age.")
    else:
        print("This customer is not of drinking age.")

# Function = A named section of code that performs a specific task 

# Math and methods

from math import sqrt

def absolute_difference(value_a, value_b):
    return abs(value_a - value_b)

def get_hypotenuse(a, b):
    return sqrt(a ** 2 + b ** 2)

def get_area_rectangle(width, height):
    return width * height

def print_area_and_hypotenuse(x1, y1, x2, y2):
    width = absolute_difference(x1, x2)
    height = absolute_difference(y1, y2)
    area = get_area_rectangle(width, height)
    hypotenuse = get_hypotenuse(width, height)
    print('Area of the rectangle is:')
    print(area)
    print('The diagonal of the rectangle is:')
    print(hypotenuse)

# Method Calls

# Methods are also called by name but are associated with an object.
# Really, they are identical to functions except that the data passed into it is passed implicitly.

#We can use the dir() function to see the methods of an object
# and help() to see what they do.

# Lists

for number in [1, 2, 3, 4]:
	print(number)

# List methods

to_dos = []
to_dos.append('publish slides')
to_dos.append('fix air conditioner'.upper())
to_dos.append('send letter')
print(to_dos)

# lists are mutable (able to be changed), and iterable (can iterate over them)toto_dos = []

to_dos.append('publish slides')
to_dos.append('fix air conditioner'.upper())
to_dos.append('send letter')
print(to_dos)_dos = []
to_dos.append('publish slides')
to_dos.append('fix air conditioner'.upper())
to_dos.append('send letter')

print(to_dos)

len(dos)

# indexing

print(to_dos[0])

print(to_dos[3])
# => throws error

print(to_dos[len(to_dos) - 1])

# Dictionaries

# sometimes called "hashmap", made up of key/value pairs
# indexed by keys

menu_categories = {
	'food': 'stuff you eat',
	'beverage': 'stuff you drink',
}

menu =
	{
	'tofu': 4,
	'soda': 2,
	'juice': 3
	}

tofu_price = menu['tofu']

menu['cake'] = 4

menu.get('cake')
# returns 4

menu.get('iced tea')
# does not return anything, and does not error out 

menu.items()
# returns list

menu_keys = menu.keys()
menu_keys = sorted(menu_keys)
print(sorted(menu_keys))

for menu_key in menu_keys:
    print(menu_key)
    print(menu[menu_key])

# The In Operator: works for both lists and dictionaries

if 'soda' in menu:
	print('yay soda')

if 'publish slides' in to_dos:
	print('better do that')

# Open a text file and do some processing

# copy helpers.py into text editor

# download book or in plain text to try (compulsory vaccination)






