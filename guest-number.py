# Guest the random number. That's comfortable with python > 3.x
import random

guessestaken=0
number = random.randint(1, 20)
print("Hello! What is your name? ")
myName = input()
print ("Well," + myName +". I am thinking of a number between 1 and 20.")
print ("And 1 condition you must know that u have just only 4 times to guess. Let's start!")
while guessestaken<=4:
	print ("Take a guess:")
	guess=input()
	guess=int(guess)
	guessestaken=guessestaken+1
	
	if(guess>number):
		print ("Your guess is too high.")
	if(guess<number):
		print ("Your guess is too low.")
	if(guess==number):
		break
if(guess==number):
	print ("Good job, "+ myName +". You were right man!")
	print ("Your guest is " + str(guess) + " that matchs with our number " + str(number))
else:
	print("Oops, it seems you go wrong man")
	print("Our number is " + str(number))

