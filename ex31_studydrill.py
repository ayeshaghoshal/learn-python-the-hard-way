# -*- coding: utf-8 -*-

print "EXERCISE 31 - Making Decisions"

# STUDY DRILLS

print "You enter a dark forest with two directions. Do you go east or west?"

door = raw_input("> ")

if door == "east":
	print "A dwarf blocks your way and asks you: How many coins do I have in my hand?"
	print "1. I don't know it"
	print "2. Less than 10"
	print "3. More than 10"
	print "4. 10"
	
	coins = raw_input("$ ")
	
	if coins =="2":
		print "Meh....Cheapskate! You will be forcefed a witch's brew! It's POISON!"
	elif coins == "3":
		print "You are right! Proceed to the garden of wealth!"
	else:
		print "Hmmm...lucky escape. You go back to the start."
	
	coins = raw_input("@ ")
		print "So, you need an anecdote and Quickly! you only have a few minutes! Anecdote is hidden in a tree. Name that tree"
		print "1. Palm tree"
		print "2. Fir tree"
		print "3. Magic floating tree"
		
	
	# MISSING A STEP SOMEWERE!!
	poison = raw_input("> ")
	
	if poison == "1" or poison == "2":
		print "You really didn't learn anything! You DIEE!"
	elif poison == "3":
		print "You are cured and know the way to the garden of wealth!"
	else:
		print "You go back to the start"

elif door == "west":
	print "You see a beautiful house made of frosting! And spot a door. What do you do?"
	print "1. You knock on the door"
	print "2. You start eating the frosting. It's too delicious!"
	print "3. You hate frosting! You head away from the house"
	
	house = raw_input("> ")
	
	if house == "1":
		print "A witch opens the door and eats you whole! You diee"
	elif house == "2":
		print "A witch catches you eating and tears you limb from limb. You diee"
	else:
		print "Good job! You resisted, coz a witch stays in that house who loves to eat humans!"
else:
	print "You are going the  worng way! And are devoured by a pack of hungry dragons"