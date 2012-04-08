# This is a guess the number game. 
import random

guessesTaken = 0

myName = raw_input("Hello! What is your name? ")

number = random.randint(1, 100)
print "Well, %s I'm thinking of a number between 1 and 100." % (myName)

while guessesTaken < 10:
    print "Take a guess." # There are four spaces in front of print.
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print "Your guess is too low."

    if guess > number:
        print "Your guess is too high."

    if guess == number:
        break


if guess == number:
    guessesTake = str(guessesTaken)
    print "Good job, %s! You guessed my number in %d guesses!" % (myName, guessesTaken)

if guess != number:
    number = str(number)
    print "Nope. The number I was thinking of was %d" % (number)
