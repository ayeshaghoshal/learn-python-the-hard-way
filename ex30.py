# -*- coding: utf-8 -*-

print "EXERCISE 30 - Else and If"

people = 30
cars = 35
trucks = 15

# 'elif' is short for "else if" and it is used for
# additional conditions, while "else" is used to
# cover anything not specifically addressed



if cars > people:
	# 40 > 30 is true so this will print and 
	# skip the "elif" and "else"
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

if trucks > cars:
	# 14> 40 is false, so the first line is skipped
	print "That's too many trucks."
elif trucks < cars:
	# 14 < 40 is true, so this line will print and
	# the "else" will be skipped
	print "Maybe we could take the trucks."
else:
	print "We still can't decide."

if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."

if people < cars or cars > trucks
		print "You got it rightt!!"

if cars != trucks:
	print "woww!"



