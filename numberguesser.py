#mark and abner are making a guessing game#
#guess the number between 1 and 100#

import random 

numOfTries = 5
numToGuess = random.randint(1, 100)
gameOver = False
print numToGuess
print

while(not gameOver and numOfTries > 0 ):
    userInput = raw_input("Please guess a number between 1 and 100 \n")
    userInput = int(userInput) #convert their guess for comparison

    print "You guessed " + str(userInput)
    numOfTries = numOfTries - 1
    
    if (userInput == numToGuess):
        print "You win! The number was" + str(numToGuess) 
        gameOver = True

    else :
        print "Nope"
        if (userInput > numToGuess):
            print "Guess lower!"

        else :
            print "Guess higher!"
        gameOver = False

if (gameOver == False):
    print "You ran out of tries, you should have guessed " + str(numToGuess)
    
