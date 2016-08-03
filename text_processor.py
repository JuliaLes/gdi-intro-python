
# GDI Intro to Python HW Problems 7/27/16

# Note: this file contains multiple versions of the same method made at
# varying stages in completion of the assignment(s). 
# To try these methods individually, they should be moved to separate
# files or the others should be commented out. 

# This program will allow the user to ascertain whether a particular word 
# is present in a large text document. The text used in this example is
# compulsory_vaccination.txt, although any .txt file would do. 
# This program is not case-sensitive. 

from helpers import generate_cleaned_lines

def is_word_in_file(word, filename):
	for line in generate_cleaned_lines(filename):
			list_of_line_words = line.lower()
			if word in line:
				print("The document " + filename + " contains the word " + word + ".")
				exit()
	print("The document " + filename + " does not contain the word " + word + ".")

# If you would like to choose your own file, un-comment the following line:
# input_file = input("Enter a .txt document to search: ")

input_word = input("Enter a word to search for: ")

# If you would like to choose your own file,
# replace 'compulsory_vaccination.txt' with input_file
is_word_in_file(input_word.lower(), 'compulsory_vaccination.txt')

##########################

# similar problem, but also returns line numbers

from helpers import generate_cleaned_lines

def is_word_in_file(word, filename):
	line_number = 0
	lines_of_found_word = []
	for line in generate_cleaned_lines(filename):
			line_number += 1
			line = line.lower()
			if word in line:
				lines_of_found_word.append(line)
	if lines_of_found_word == []:
			print("The document " + filename + " does not contain the word " + word + ".")
	else
			print("The document " + filename + " contains the word " + word + ".")
			print("It can be found on lines: " + ", ".join(str(line_num) for line_num in lines_of_found_word))
				

# If you would like to choose your own file, un-comment the following line:
# input_file = input("Enter a .txt document to search: ")

input_word = input("Enter a word to search for: ")

# If you would like to choose your own file,
# replace 'compulsory_vaccination.txt' with input_file
is_word_in_file(input_word.lower(), 'compulsory_vaccination.txt')

##########################

# similar problem, but also returns each word with the number of times it occured

from helpers import generate_cleaned_lines

def is_word_in_file(word, filename):
	dictionary = dict()
	for line in generate_cleaned_lines(filename):
			list_of_line_words = line.lower().split()
			for word in list_of_line_words:
				dictionary[word] = dictionary.get(word, 0) + 1
	print(dictionary)

# If you would like to choose your own file, un-comment the following line:
# input_file = input("Enter a .txt document to search: ")

input_word = input("Enter a word to search for: ")

# If you would like to choose your own file,
# replace 'compulsory_vaccination.txt' with input_file
is_word_in_file(input_word.lower(), 'compulsory_vaccination.txt')