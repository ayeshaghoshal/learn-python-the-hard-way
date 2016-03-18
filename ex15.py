# -*- coding: utf-8 -*-

print "EXERCISE 15 - Reading Files"

# Lines 6-8 uses 'argv' to get a filename
from sys import argv

script, filename = argv

# introduce a new command 'open' - Open a file, returning an object of the file type
# 'open' is similar to the functions when you write own scripts as raw_input,
# it takes a parameter and returns a value you can set to your own variable.
#Variable in this case would be 'txt' that is to be defined by the argument 'filename'
txt = open(filename)

#prints the message that you want to be displayed on command line
print "Here's your file %r:" % filename
# syntax to use to read a text file - empty brackets denotes that the command is executed without any parameters
print txt.read()
txt.close()

# repeating the file again - the string would come up on command line 
print "Type the filename again:"
# this line requires the user to plug in the name of the text file after the ">"
file_again = raw_input("> ")
# gives the command that once the file name is written correctly, while file name is to be opened
txt_again = open(file_again)
# denotes what is to be read when the specific file name is opened
print txt_again.read()
txt.close()

# Study drill to review again!!!
# Get rid of the lines 23-29 where you use raw_input and run the script again.
# Use only raw_input and try the script that way. Why is one way of getting the filename better than another?
# Start python to start the python shell, and use open from the prompt just like in this program. Notice how you can open files and run read on them from within python?
