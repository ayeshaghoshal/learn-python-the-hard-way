# -*- coding: utf-8 -*-

print "EXERCISE 13 - Parameters, Unpacking, Variables"

# use of an 'import' feature
# argv is the 'argument variable' - 
# the variable holds the agruments you intend to use when python runs your code
from sys import argv

# 'unpacks the argv variable in the sys feature, in the sense that all the values of argv gets assigned to 
# 4 seperate variables that need to be highlighted in the command line
# analogy - It just says, "Take whatever is in argv, unpack it, and assign it to all of these variables on the left in order."
script, first, second, third, fourth = argv
# 'sys' features that can be imported from the universal Python universe are called MODULES

x = raw_input("What is your name?")
# y = int(raw_input("For how many days have you been here?"))


print "The script is called:", script
print " Hi %r!" % (x)
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth


day_one = raw_input("What day of the week is it? ")
day_two = int(raw_input("How old are you today? "))

# print "You are %d years old this %r!" % (day_one, day_two)
# The line above is wrong! WHY?? - %d can only be assigned an integer value in the brakets

print "So, %r is %s years old on a %r!" % (x, day_two, day_one)



# 'ValueError: need more than 3 values to unpack' 
# The above happens when you don't put enough number of arguments on the command line