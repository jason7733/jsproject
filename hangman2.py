# hangman2.py - Pratice for hangman. It's comfortable with Python >= 3.x version
import random
# The quote ''' content ''' means the content is on multiple line
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()


# do you want to play again
def playAgain():
	print("Do you wanna play again? [Y]es or [N]o: ")
	return input().lower().startwith('y')
def randWord(wordList):
	i = randint(0, len(wordList-1))
	return wordList[i]
def displayBoard(HANGMANPICS,wrongLetters,correctLetters,missedLetters)
	
