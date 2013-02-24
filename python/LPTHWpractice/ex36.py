from sys import exit

# engine room is where the adventure begins
# the user can go north or east
# they wake up in this room 
def engine_room():
	print "You wake in a huge star ship's engine room. You do not remember how you got here. "
	print "A blinking red light flashes above your head, and you hear warning sounds."
	print "Somewhere in the cobwebs of your mind, you think, 'Red Alert!'"
	print "You have two exits. A heavy door located to the East, and another to the North."
	print "What do you do?"
	print "1. Go North."
	print "2. Go East."

	next = raw_input("> ")

	if "1" in next:
		stairway_room()
	elif "2" in next:
		armory_room()
	else:
		print "What are you talking about? Did you get hit on the head?"
		engine_room()

# armory is a dead end room 
# it has guns, armored vests
# the user can pick these up and put them in their inventory
def armory_room():
	print "[enter description]"
	print "[enter choices]"



# stairway is a room that only has an exit up
def stairway_room():
	print "[enter description]"


# a need user controls
# the user can enter directions (n, s, e, w)
# the user can pickup items (add to list)
# user can view inventory (view list)

engine_room()
