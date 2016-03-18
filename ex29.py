# -*- coding: utf-8 -*-

print "EXERCISE 29 - What if"

people = 200
cats = 45
dogs = 100

if people < cats:
	print "Too many cats! The world is doomed!"

if people > cats:
	print "Not many cats! The world is saved!"

if people < dogs:
	print "The world is drooled on!"

if people > dogs:
	print "The world is dry!"

# increment operator. Means dogs = dogs + 5 = 100 + 5
dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."

if people <= dogs:
	print "People are less than or equal to dogs."

if people == dogs:
	print "People are dogs."

if cats == 45:
	print "Thaaat's right!!"

if people >= cats + dogs:
	print "People rulee!!"
	

# STUDY DRILLS

# if-statement: it's a condition that is to be obeyed by the set parameters
# why indented? the if-statement will only apply to the indented code otherwise, there's an indentationError


# Actual explaination!!

# if-statement - creates what is called a "branch" in the code. The if-statement tells your script, 
#      "If this boolean expression is True, then run the code under it, otherwise skip it.

# why indented? - A colon at the end of a line is how you tell Python you are going to 
#    create a new "block" of code, and then indenting four spaces tells Python what lines of 
#    code are in that block. 
#    This is exactly the same thing you did when you made functions in the first half of the book.

# If not indented? - will most likely create a Python error. 
#     Python expects you to indent something after you end a line with a : (colon)

# 


