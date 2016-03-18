# -*- coding: utf-8 -*-

print "EXERCISE 16 - Reading & Writing Files"

#STUDY DRILLS
# Write a script similar to the last exercise that uses read and argv to read the file you just created.

from sys import argv

script, filename = argv

# this syntax opens the file
magic = open(filename)

print "Here's your file %r " % filename
print magic.read()

print "Now to close the file!"
magic.close()