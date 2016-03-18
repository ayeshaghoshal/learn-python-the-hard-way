# -*- coding: utf-8 -*-

print "EXERCISE 14 - Prompting and Passing"

# Using the 'argv' and 'raw_input' commands together to ask the user something specific

# 'sys' module to import the argument from 
from sys import argv

# define the number of arguments that need to be defined on the command line
script, user_name = argv
# instead of using raw_data in the previous formats, this is a new way. 
# Defines what character will show up when a raw input is required by the user
prompt = '@ '

# 
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
# the following line defines that a prompt is required by the user 
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

# Use of triple brackets and % command together to combine string and raw input data
# since this line of code comes after 'likes', 'lives' and 'computer', we know what value to insert
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

