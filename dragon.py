# This's comfortable with Python > 3.x version
# import random
import time

def displayIntro():
	print("You're in a dragon land with 2 caves. One of them")
	print("is a kind dragon's cave, he will share his treasure with you.")
	print("And other is greedy and hungry, he will eat you on sigh.")
	print()

def chooseCave():
	cave=''
	if cave!=1 and cave!=2:
		print ("Please choose your cave: ")
		cave=input()
	return cave

def checkCave(choosenCave):
	print("You've approached the cave....")
	time.sleep(2)
	print("It's dark and spooky...")
	time.sleep(2)
	print("A huge dragon jumps out in front of you! He open his jaws and...")
	print()
	time.sleep(2)

	#friendlyCave=random.randinit(1,2)
	friendlyCave=1	
	if choosenCave==str(friendlyCave):
		print("Give you his treasure.")
	else:
		print("Gobbles you down in one bite")

playAgain='yes'
while playAgain=='yes' or playAgain=='y':
	displayIntro()
	choosenCave=chooseCave()
	checkCave(choosenCave)
	print("Do you want to play again ([Y]es or [No]):")
	playAgain=input()

