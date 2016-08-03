# class 4
# 8/2/16

# url for slides: http://byssystems.com/gdi/#/

# some review

# methods are called on objects, functions are not called on anything, instead things are passed to them
# differentiation is relevant because you can make your own objects and choose which methods can act on them

# all collections (lists, dictionaries, etc) are iterable
# in python, 'yields' usually implies iterable

for thing in things:
	print(thing + "is a thing")

# collection methods

  len() # length
  range() # creates a list in given range
  range(n) # creates list with ints 0 through n-1
  range(x,y) # creates list x though y-1
  range(x,y,z) # creates list x though y-1, by intervals of z starting at x

 return(len(range(5,10))) => '5'

 sorted() # sorted list
 enumerate() # returns a list of (index, element) from the list
 zip() # Given one or more iterables, returns a list of tuples with an element from each iterable

# tuple = series of immutable Python objects, like lists
# but unlike lists cannot be changed and use parentheses

# in
menu = {'carrot': 5, 'burger': 2}
return('tapas' in menu) => False
return('burger' in menu) => True
return(5 in menu) => False