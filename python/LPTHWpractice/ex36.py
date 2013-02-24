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
	print "You enter a dead end room"
	print "but it seems to be an armory."
	print "there are guns and armored vests"
	print "wil you take them?"
	print "type yes if you do, type no if you wish to return to the engine room"
	
	next = raw_input("> ")
 #enter in the options for inventory when we figure out how to
 #it will be a list to show items we pick up along the journey
 #the player will have to be able to access the inventory at any time   
    


# stairway is a room that only has an exit up
def stairway_room():
	print "you enter and see a staircase, a cramped foggy area surrounds you."
	print "do you go up the stairs or go back?"
	print " type up to go up the staircase type back to return to the enine room"
	
	next = raw_input("> ")
	
	if "up" in next:
		bridge_room()
	elif "back" in next:
		engine_room()
	else:
		print "I do not understand this command"
		stairway_room()

#the bridge is a room that consists of a mini game
#and a elevator that goes only up

def bridge_room():
	print "you enter the bridge. you look and see a vast open area."
	print "there are windows and you stare at the vast open space."
	print "there is a control pannel infront of you"
	print "do you go and explore?"
	print "type yes if you wish to explore, type no if you look around more."
	
	next = raw_input("> ")
	
	if "yes" in next:
		control_game()
	elif "no" in next:
		observation_elevator()
	else:
		print"i dont understand this command"
        
#the control mini game is a game were you press numbers
#a string of events happens when you press different numbers
#a few things are obtained WE NEED TO FIGURE OUT THE INVENTORY!!!
def control_game():
	print "when you get to the control pannel you see a bunch of numbers"
	print "the controls are simple press a number from 1-5 to see what happenes"
	
	next = raw_input("> ")
	
	if "1" in next:
		print "a red and green parrot swoops down"
		print "and lands on your shoulder. sings merry christmas and flys away"
	elif "2" in next:
		print"a cookie is obtained"
	elif "3" in next:
		print "a parrot flies to your shoulder."
		print "you obtain it"
	elif "4" in next:
		print "sparks fly everywere!!"
		print "the pannel dies"
		bridge_room()
	elif "5" in next:
		print "all of a sudden a voice like wind whispers in your ear"
		print "you are captvated by it."
		print "you break out of the trance"
	elif "go back" in next:
		bridge_room()
	else:
		print"i dont understand this command"
 
 
 
 
# a need user controls
# the user can enter directions (n, s, e, w)
# the user can pickup items (add to list)
# user can view inventory (view list)

def start (): 
	print "Starbizzel is an text-based adventure set in a universe with advanced technology."
	print "To play, you press a number for the choice you wish to take."
	print "Have fun and good luck."
	engine_room()

start ()
