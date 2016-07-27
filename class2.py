# class 2
# 7/19/16

# Playing with conditionals

input_value = input("Enter a number: ")
x = int(input_value)
if x == 2:
	print('Your number is equal to 2')
elif x > 100:
	print('Your number is greater than 100')
elif x % 5 == 0:
	print('Your number is a multiple of five and less than 100')
else:
	print('Your number is not equal to 2, is less than 100, and is not a multiple of 5')
print('Done evaluating number.')

# Iterations

input_value = input("Enter a number: ")
y = int(input_value)
while y > 0:
	print(y)
	y -= 1
print('Done')

# For Loop

numbers = [1,2,3,4]
for num in numbers:
	print("The current number is: " + str(num))

# While loop

input_value = False

while input_value != "yes":
	input_value = input("Do you like pita chips? ")
print('Good!')


# Function calls

a = 3
print(type(a))

# Define functions

def print_plus_5(x):
	print(x + 5)


def plus_5(y):
	return y + 5

print(plus_5(4))

def area_of_rectangle(width, height):
	return width * height

def rectangle_area():
	width = int(input("Enter a width: "))
	height = int(input("Enter a height: "))
	return width * height

print(rectangle_area())




