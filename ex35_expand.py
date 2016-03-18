# -*- coding: utf-8 -*-

print "EXERCISE 35 - Branches and functions addition to game"

from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take? Enter a number"
	
	choice = raw_input("> ")
	if choice.isdigit(): # Better test - tests if all characters in a string are decimal digit (0-9)
		how_much = int(choice)
	else: 
		dead("Man, learn to type a number.")

		
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")
		

def diamond_room():
	print "You are in a room full of diamonds!"
	print "how many diamonds would you take?"
	
	while True: 
		choice = raw_input("> ")
		if choice.isdigit():
			next = int(choice)
		else:
			dead ("I can't understand what you have written")
				
		
		if next > 100:
			print " You are too greedy!!"
		elif next < 50:
			print "not bad! You are a decent human being. You keep all the diamonds in the room!"
			exit(0)
		else:
			dead("Not going to happen!")


def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		choice = raw_input("> ")
		
		if choice == "take honey":
			dead("The bear looks at you then slaps your off.")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through now"
			bear_moved = True
		elif choice == "taunt" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."


def cthulhu_room():
	print "Here you see the great evil Cthulhu"
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	choice = raw_input("> ")
	
	if "flee" in choice:
		start()
	elif "head" in choice:
		diamond_room()
	else:
		cthulhu_room()


def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "You are in a dark room"
	print "There is a door to your right and left"
	print "Which one do you take?"
	
	choice = raw_input("> ")

	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead ("You stumble around the room until you starve")


start()