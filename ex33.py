# -*- coding: utf-8 -*-

print "EXERCISE 33- While loops"

# A while-loop will keep executing the code block under it as long as a boolean expression is True.
#What they do is simply do a test like an if-statement, but instead of running the code block once,
	# they jump back to the "top" where the while is, and repeat. 
	# while-loop runs until the expression is False.

# problem with while-loops: Sometimes they do not stop
	# Make sure that you use while-loops sparingly. Usually a for-loop is better.
	# Review your while statements and make sure that the boolean test will become False at some point.
	# When in doubt, print out your test variable at the top and bottom of the while-loop to see what it's doing
	

i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)

	i = i + 2
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
	print num

numbers = []



# STUDY DRILLS

def number_1(x):

	i = 0
	while i < x:
		print "At the top i is %d" % i 
		
		i += 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

print "Pick a random number: "
x = raw_input()

print "The numbers are: "
number_1(int(x))
# int() is required coz raw_input returns a string.
#when you pass it to your function, you're comparing an integer and a string
# need to deternmine that the raw_input is classified as a number and acts in such a way



