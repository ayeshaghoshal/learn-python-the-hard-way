# -*- coding: utf-8 -*-

print "EXERCISE 16 - Reading & Writing Files"

# specify which part of the 'sys' module will need to be extracted
from sys import argv

# define the data within 'argv'
script, filename = argv

print "We're going to erase %r. " % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
#commonly-used values of mode are 'r' for reading, 
#'w' for writing (truncating the file if it already exists), and 'a' for appending
#  If mode is omitted, it defaults to 'r'.
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
line4 = raw_input("line 4: ")

print "I'm going to write these to the file."


target.write ("%s\n%s\n%s\n%s" % (line1, line2, line3, line4))
#target.write(line1 + "\n" + line2 + "\n" + line3 + "\n" + line4)
#targe.write ("{0}\n{1}\n{2}\n".format(line1,line2,line3))
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print "And finally, we close it."
target.close()