# -*- coding: utf-8 -*-

print "EXERCISE 17 - More Files"

from sys import argv
# import another handy command named exists - returns True if a file exists
#based on its name in a string as an argument. It returns False if not
from os.path import exists

script, from_file, to_file = argv 

# string to identify what names of files are to be displayed
print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

#the single line method to write the above codes
#indata = (open(from_file)).read()

# len() measures length of the string that you pass to it then returns that as a number
print "The input file is %d bytes long" % len(indata)

# query about whether the to_file actually is saved in system - True or False  
print "Does the output file exist? %r" % exists(to_file)
# give the command as to whether you want to copy the data from one file to another
print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input input is required to fulfill the command given above - RETURN or CTRL-C 
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

# (open.(to_file, 'w')).write(indata)
print "Alrigt, all done."

out_file.close()
in_file.close()