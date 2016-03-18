# -*- coding: utf-8 -*-

print "EXERCISE 33- While loops"

# use of for-loop and range to define the bottom and top numbers in the list 
# 	instead of a while-loop 

prop = []

for y in range(0, 6):
	print "At the top y is %d" % y
	prop.append(y)

	y += 1
	print "At the bottom y is %d" % y

print y 