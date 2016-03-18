# -*- coding: utf-8 -*-

print "EXERCISE 20 - Functions and Files"

from sys import argv

script, input_file = argv

# define function to print out and read out the whole file - (f) means file that needs to be read out
def print_all(f):
# commands the file to be read out completly
	print f.read()

# function that tells the file (f) to be reset back to the beginning of the file
def rewind(f):
# The code seek(0) moves the file to the 0 byte (first byte) in the file.
	f.seek(0)

# define a function that specifies which exact line that needs to be printed
# within brackets - 1st parameter defines the line number to be read, 2nd is the file variable
def print_a_line(line_count, f):
# the following line prints the line number and uses the f.readline function to determine which line is to be read
	print line_count, f.readline()

# function to actually open a specific file that is to be stated in the command line	
current_file = open(input_file)

print "First, let's print the whole file:\n"

# use of defined function to print the whole file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# use of defined function to go back to the beginning of the file
rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1 # this line number advancement prompt is not necessary. .readline automatically advances the line number everytime its been called
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

# for the benefit of the previous 6 lines, here's the explaination:
# A file object advances every time you call .readline() on it; 
# the 'current_line' variable is only used to give you a line number. 
# The two are not really related.

# You can imagine current_line to be your own personal notepad keeping a count, 
# just to verify that the lines are indeed advancing. 
# If you forget to write down the next number, the file doesn't care and moves on regardless.

