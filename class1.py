# class 1
# 7/11/16

# Write a function that takes an input and does something with it

# Variables, inputs, basic methods

# radius of a circle

input_value = input("Enter a radius:")
radius = float(input_value)
area = 3.14159 * radius * radius
print("The area of a circle with radius " + input_value + " is: " + str(area))

# convert mm to diopters

input_val = input("Enter a focal length in mm: ")
focal_length = float(input_val)
diopters = 100 / focal_length
print("The dioptric value for a " + input_val + "mm focal length is: " + str(diopters) + "D")

# favorite tea

input_val = input("What is your favorite type of tea? ")
if (input_val.lower() == 'rooibos'):
	print("Rooibos is also my favorite type of tea!")
else:
	print(input_val + "sounds great!")