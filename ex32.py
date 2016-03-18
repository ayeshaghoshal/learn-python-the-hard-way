# -*- coding: utf-8 -*-

print "EXERCISE 32 - Loops and Lists"

# use a for-loop in this exercise to build and print various lists
# Before you can use a for-loop, you need a way to store the results of loops somewhere
# best way to do this is with lists
# You start the list with the [ (left bracket) which "opens" the list
	# Then you put each item you want in the list separated by commas
	# Lastly, end the list with a ] (right bracket) to indicate that it's over
	#  Python then takes this list and all its contents and assigns them to the variable

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i
	

# we can also build lists, first start with an empty one
elements = []
# then use the range function to do 0 to 5 counts
for i in range(0,6):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i)
	
# now we can print them out too
for i in elements:
	print "Element was: %d" % i

# example of range function
for x in range(10,50,5):
	print x
# range([start], stop[, step])
#	start: Starting number of the sequence
#	stop: Generate numbers up to, but not including this number
#	step: Difference between each number in the sequence
#	All parameters must be integers
#	The syntax to access the first element of a list is mylist[0]


#	STUDY DRILLS
# Could you have avoided that for-loop entirely on line 22 and just assigned range(0,6) directly to elements?
#	The key word here is "assigned". In Python, we assign things with =. Hint, hint

elements = range(0, 6)

for i in elements:
	print "Element was: %d" % i

#What other operations can you do to lists besides append?
#	http://www.tutorialspoint.com/python/python_lists.htm

