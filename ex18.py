# -*- coding: utf-8 -*-

print "EXERCISE 18 - Names, Variables, Code and Functions"

# Functions do 3 things:
# - They name pieces of code the way variables name strings and numbers
# - They take arguments the way your scripts take argv.
# - Using 1 and 2 they let you make your own "mini-scripts" or "tiny commands."

# !!!! create a function by using the word 'def' in Python !!!!!

#this one is like your scripts with argv 
def print_two(*args):
# following line unpacks the parameters that define *args 
	arg1, arg2 = args
# denotes what is to be printed when the function 'print_two' is used
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# ok, that *args ia actually pointless, we can just do this
def print_two_again(arg1,arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one arguments
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
# when there is nothing in terms of paraments inside the brackets 
	print "I got nothin'."

# the following lines of code are the functions used to print functions on the command line 
print_two("Peanuts", "Flowers")
# 'print_two_again' needs 2 strings to be defined for the function to be displayed 
print_two_again("Zed", "Animals")
print_one("No way!")
print_none()
# used the same function to define two seperate paramenters
print_two("Does this work?")


# BREAK DOWN OF DEFINING FUNCTIONS!
# First we tell Python we want to make a function using def for "define".
#On the same line as def we give the function a name. In this case we just called it "print_two" but it could also be "peanuts". 
#It doesn't matter, except that your function should have a short name that says what it does.
#Then we tell it we want *args (asterisk args) which is a lot like your argv parameter but for functions. This has to go inside () parentheses to work.
#Then we end this line with a : colon, and start indenting.
#After the colon all the lines that are indented four spaces will become attached to this name, print_two. 
#Our first indented line is one that unpacks the arguments the same as with your scripts.
#To demonstrate how it works we print these arguments out, just like we would in a script.
