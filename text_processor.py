
# GDI Intro to Python HW Problem 7/27/16

# This program will allow the user to ascertain whether a particular word 
# is present in a large text document. The text used in this example is
# compulsory_vaccination.txt, although any .txt file would do. 
# This program is not case-sensitive. 

from helpers import generate_cleaned_lines

def is_word_in_file(word, filename):
	for line in generate_cleaned_lines(filename):
			list_of_line_words = line.lower().split()
			if word in list_of_line_words:
				print("The document " + filename + " contains the word " + word + ".")
				exit()
	print("The document " + filename + " does not contain the word " + word + ".")

# If you would like to choose your own file, un-comment the following line:
# input_file = input("Enter a .txt document to search: ")

input_word = input("Enter a word to search for: ")

# If you would like to choose your own file, replace
# replace 'compulsory_vaccination.txt' with input_file
is_word_in_file(input_word.lower(), 'compulsory_vaccination.txt')
