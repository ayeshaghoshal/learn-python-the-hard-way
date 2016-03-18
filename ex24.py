# -*- coding: utf-8 -*-

print "EXERCISE 24 - More Practice"

print "Let's practice everything"
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\t The lovely world
\twith logic so firmly planted
\tcannot discern \n the needs of love 
\tnor comprehend passion from intuition
\tand requires an explaination
\n\twhere there is none.
"""

print "_____________"
print poem
print "_____________"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 1000
	return jelly_beans, jars, crates
	

start_point = 10000
# since jelly_beans is a variable, the name of the ssid variable can be changed e.g to 
# 'beans' and moving forward, beans would be hte new name of the same variable
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates" % (beans, jars, crates)

# the below 1st start_point = manipulate the previous value of start_point
# to result in the new value
start_point = start_point / 20

print "We can also do that this way:"

# using the function and the defined start_point parameter above to result in the values 
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

def numbers(input):
# the 'input * 10' commands the expression to be repeated 10 times
	print "I have %d cars!" % input * 10  
	return input * 2

a = numbers(10)

print "NOw that amounts to %d cars" % a







