import random
magicNumber = random.randint(1, 10)

userGuess = int(input ("\nInput a number: "))

if userGuess == magicNumber:
   # print (magicNumber, "That's a match - yay!")
    print ("You guessed", userGuess, "The number matched", magicNumber)
elif userGuess == magicNumber +1 or userGuess == magicNumber -1:
    print ("Very close")
    print ("The Magic Number was:", magicNumber)
else:
    print("Try again")
    print ("The Magic Number was:", magicNumber)
