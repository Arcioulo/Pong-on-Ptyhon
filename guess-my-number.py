# Guessing Game
# Computer chooses a random number from MIN to MAX. User has TRIES tries
# Abner Coimbre (@abnercoimbre)
import 
from random import randint

MIN = 1
MAX = 100

num = randint(MIN, MAX)

print "I'm thinking of a number between " + str(MIN) + " and " + str(MAX) + "..."

guess = int(raw_input("Guess: "))
tries = 1

while guess != num and tries < 5:
    if guess > num:
        print "Lower..."
    else:
        print "Higher..."

    guess = int(raw_input("Guess: "))
    tries += 1

if guess == num:
    print "Congrats!"
else:
    print "Damn... You lost, brah."

print "The number was ", num

raw_input("Press any key to exit.")
