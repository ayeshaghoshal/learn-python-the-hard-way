# -*- coding: utf-8 -*-

print "EXERCISE 37 - Symbol Review"


# and, as, boolean  values, with x as y  

print True and False == False

x = True
y = False

if True or False:
	print "The answer is %s" % x

if True and not False:
	print "This time round, the answer will be %s" % x 

if not False or not (True and False):
	print "Yet again, the answer is %s" % x 
	

with open("37sample.txt", 'w') as sample: 
	sample.write("Hi there!") # open a new file to write in or open an existing file to be read 
	

	
	
	
# def, assertion, return

# assertion is used to make sure the internal program written is as the programmer intended it to be, with the goal of catching bugs
# assertions should be used when your code SHOULD NOT ever reach a point, meaning there is a bug there


def KelvinToFahrenheit(Temperature):
	assert (Temperature >= 0),"Colder than absolute zero!"
	return ((Temperature-273)*1.8)+32

print KelvinToFahrenheit(273)
print int(KelvinToFahrenheit(505.78))
print KelvinToFahrenheit(-5)

def test_set_comparison():
	set1 = set ("1347")
	set2 = set ("3245")
   assert set1 == set2
	
test_set_comparison()

# break and continue for loops

for letter in 'howdy':   	# 1st example
		if letter == 'd':
			break
		print "Curent Letter is: ", letter

num = 100
while num >= 100:
	print "Curent value is: ", num
	num = num + 2 
	if num == 110:
		break

for num in range(2,15):
	if num % 2 == 0:
		print "This is an even number.", num
		continue
	print "This is an odd number.", num
	
	
print "Good Bye!"





# Class function - Like its colsely related cousin def, Class is used to define a class.
# Class is a logical grouping of large grouping of data and functions ("funcions" are frequently referred to 'method' when defined within a class)
# The grouping defined within a class can have functions attached to them. These grouping are not meant to be random.
# They can be based on objects in the real world (Customer data, product data) or logical concepts within Python.

class Product(object): # we've merely outlined the blueprint to create a Product object
	""" A product launched to be sold. The product has the followint properties:
	
	Attributes: 
		name of product: A string representing the product name
		value: initial price the product is to be sold at
	"""

def __init__(self, name, value=10):
		"""Return a Product object whose name is *name* and starting
        price is *value*."""
		self.name = name
		self.value = value

def sell(self,selling_price):
	"""Return the value for which the product was actually sold for."""
	if selling_price < self.value:
		raise RuntimeError('Price of product is too low') # raise an exception when something is expected to go wrong with the code.
	selling_price -= self.value
	return self.value
	
# the class blueprint can almost be operted as a function: Soap = product('soap', 200)
# We can, of course, create as many Product objects as we'd like




# Try and Finally and Except
"""If an error is encountered, a try block code execution is stopped and transferred
down to the except block"""

try:
	print "Hello world!"
except:
	print "This is an error message!"
	
	
# try to ask for an integer number

while True:
	try:
		n = int(raw_input('Please enter an integer: '))
		n = int(n)
		break
	except ValueError
		print "This not a valid integer. Please try again!"
print "Great job! You know your numbers!"


try:
    x = float(raw_input("Your number: "))
    division = 10 / x
except ValueError:
    print "You should have given either an int or a float"
except ZeroDivisionError:
    print "not real!"
finally:
    print("There may or may not have been an exception.")


	
	
# global and local

def sue():
	x = "what to do?"
	print x 
	
sue()
print x 
# the above code won't work: especially the 2nd print x outside the def function. varaible x outside the def function ahs not been defined therefore, no global definition
# however, if we use the global statement, see what happens:

def sue():
	global x 
	x = "Wwhat to do?"
	print x 
	
sue()
print x 
# with global, the variable x will become available "outside" the scope of the function, effectively becoming a global variable.
# You can use a global variable in other functions by declaring it as global in each function that assigns to it








