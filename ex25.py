# -*- coding: utf-8 -*-

print "EXERCISE 25 - Even More Practice"

def break_words(stuff):
	""" This function will break up words for us."""
	# .split is an existing function in python that splits words in a sentence
	words = stuff.split(' ')
	# 'return' doesn't print the sentence, it just makes the modified sentence available
	return words

# typically, tend to take the result of the above 'words' and feed it into the below parameter of 'words'
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_word(words):
	""" Prints the first word after popping it off."""
	word = words.pop(0)
	print word # use of 'print' instead of 'return' since only one word has to be identified

def print_last_word(words):
	""" Prints the last word after popping it off."""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	""" Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	""" Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	""" Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

# Instructions:

# 1. start python
# 2. import this newly defined module >>> import ex25
# Note. : Don't type '.py' or you will get an error
# 3. create an object to work with
# >>> sentence = "All good things come to those who wait."

# You can avoid typing 'ex25' at the beginning
# of everythin if you import the odule like this instead:
# >>> from ex25 import *
# The n you can run the command line like this:
# sentence = "All good things come to those who wait"
# print break_words(sentence)
