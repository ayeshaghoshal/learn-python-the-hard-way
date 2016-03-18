# -*- coding: utf-8 -*-

print "EXERCISE 35 - Branches and functions"

#from 'system' (a module), you import exit (which is a function) 
from sys import exit

# gold_room is the prize to be won. 1st function to be defined
def gold_room():
	# prompt to ask the value 
	print "This room is full of gold. How much do you take?" 
	
	# raw_input designated to variable 'choice', saves the raw_input as a string  
	choice = raw_input("> ")
	# condition to set the numbers that are feasible for winning. the value needs to contain '0' or '1'
	if "0" in choice or "1" in choice:
		# converts the inputted number from above into an integer
		how_much = int(choice)
	else: 
		# introduce a new argument called 'dead' - contents in inside brackets will be printed
		dead("Man, learn to type a number.")

	# next step in the code once no. has been determined. conditions placed on value of how_much		
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		# exit is a system function imported above.
		# 0 is a code for an error-free exit
		exit(0)
	else:
		# used same variable - changed the contents of the variable
		dead("You greedy bastard! you're dead!")
		
# 2nd function to be defined 
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	# 'bear_moved' is a boolean variable and is assigned 'False' to it 
	bear_moved = False

	# create a loop to ask the above question again until you enter the right answer	
	while True:
		# 'choice' variable use in above function too
		# Is possible to ise same variable since it's being used in a seperate function above - local variabble
		choice = raw_input("> ")
# conditions below will class bear_moved as False and run the program		
		# condition placed on the raw_input entered
		if choice == "take honey":
			# another version of same variable 'dead' - diiferent function
			dead("The bear looks at you then slaps your off.")
		# if choice == taunt bear is True and if bear_moved is also True as indicated two lines below
		# Then the script stated one line below will be displayed
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through now"
			
# after runnng program with 'bear_moved' as False, the variable 'bear_moved = True	
			bear_moved = True
		elif choice == "taunt" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			# function gold_room has been defined above
			gold_room()
		else:
			print "I got no idea what that means."


def cthulhu_room():
	print "Here you see the great evil Cthulhu"
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	# used same variable to prampt raw_input
	choice = raw_input("> ")
	# player can write whole sentence. Pythin only interested in identifying the word 'flee'
	if "flee" in choice:
		# function 'start' is defined at the bottom
		start()
	# # player can write whole sentence. Pythin only interested in identifying the word 'head'
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()
# if enter both 'flee' and 'head', python will always look for 'flee' first!

# function of 'dead' is defined multiple times. takes a single argument
# 'why' is designated various scrips above.
def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "You are in a dark room"
	print "There us a door to your right and left"
	print "Which one do you take?"
	
	choice = raw_input("> ")
	# if left, directs to the bear_room
	if choice == "left":
		bear_room() # defined above
	# if right, directs to the cthulhu_room
	elif choice == "right": 
		cthulhu_room() # defined above 
	else:
		dead ("You stumble around the room until you starve")


start()
# function "start" is defined above
# This is the only function automatically run in this code 