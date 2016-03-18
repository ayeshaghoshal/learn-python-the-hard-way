# -*- coding: utf-8 -*-

print "EXERCISE 19 - Functions and Variables"

# defining the function that commands the following strings to be printed out 
# there are 2 parameters that have to be defined in brackets
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# use of the parameters is the same method as writing string and designating values to it
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man, that's enough for a party!"
	print "Get a blanket.\n"

# a new method of displaying the function directly by designating it values
print "We can just give the function numbers directly:"
# the following function will promth the command to print the stated 4 sentences above
cheese_and_crackers(20,30)

# another method of printing the same function
print "OR, we can use variables from our script:"
# designate a value to new variables
amt_of_cheese = 10
amt_of_crackers = 30

# the new variables will replace the old parameters to state the defined values right above
cheese_and_crackers(amt_of_cheese,amt_of_crackers)

# use just numbers to define the two parameters inside the defined function
print "We can even do math inside too:"
cheese_and_crackers(20 + 25, 48 + 50)

# Showcases the use of both variables and math to display the defined function 
# as long as there are only 2 paramenters defined within the brackets!!!
print "And we can combine the two, variables and math:"
cheese_and_crackers(amt_of_cheese + 20, amt_of_crackers + 450)

#STUDY DRILLS - NEW FUNCTION!

def animals_on_farm(cows, chickens, sheep):
	print "Can you spot %d cows?" % cows
	print "I bet you won't be able to identify %d red chickens!" % chickens
	print "Did you sheer all %d sheep this season?" % sheep
	print "I hope so! otherwise they will all look like cotton balls! HAHAHA\n"	

animals_on_farm(10, 4, 23)

animals_on_farm(3 + 4, 51 + 1, 2 + 7)

a = 20
b = 14
c = 24
# can replace the name of parameters inside the function ()
animals_on_farm(a, b, c)

animals_on_farm(a + 2, b*2, c - 10)

print "We can assign the function to a variable and simply call it by its new variable name"
poo = animals_on_farm
poo(2, 4, 8)

print "We can pass a function as arguments"
print "Now ask the user for the number of cows, chickens and sheep! - brackets within brackets"
animals_on_farm(int(raw_input("How many cows?")), int(raw_input("How many chickens?")), int(raw_input("How many sheep?)")))


