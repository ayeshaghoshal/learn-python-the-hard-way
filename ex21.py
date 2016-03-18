# -*- coding: utf-8 -*-

print "EXERCISE 21 - Functions can return something"

def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b 

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b 

print "Let's do some math with just functions!"

age = add(30, 5)	
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(120, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = multiply(age, divide(height, subtract(weight, divide(age, 2))))

print "That becomes: ", what, "Can you do it by hand?"

# STUDY DRILLS
# return function:
def anything(a):
	return a + 256, a * 20, 2 * a + 100

print "So what do we have here!"
x = anything(5)
print "The calculation amounts to %d people across %d cars plus %d children!" % x

	

