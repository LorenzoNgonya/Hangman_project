# In this milestone I will use the Object Oriented Programming to develop the whole Hangman game
word_list = ["papayas","bananas","grapes","strawberries", "avocado"]
print (word_list)

from opcode import hasjabs
import random
from re import S, X
from string import ascii_lowercase










word = random.choice(word_list)
print(word)

# code that will continuously ask the user for a letter and validate it.

# while True:
#     guess = input ("guess a letter ")
#     if len(guess) ==1 and guess in ascii_lowercase: # checks that code is a single alphabetical character 
#         break
#     else :
#         print ("Invalid letter. Please, enter a single alphabetical character.")
        
# Checks if the letter guessed by the user is in the secret word that was randomly chosen by the computer. 

# if guess in word:  # if statement that checks if the guess is in the word.
#     print ("Good guess! {} is in the word.".format(guess))
# else:
#        print ("Sorry, {} is not in the word. Try again.".format(guess)) # This code will run if the guess is not in the word.

# code for the hangman classs to develop rest of the game 

class Hangman:
#      __init__ method to initialise the attributes of the class. Word_list and num_lives as parameters.
    def __init__(self, word_list, num_lives=5):

# Initialises the following attributes:
        self.word = random.choice(word_list)
        self.word_guessed = ['_ '*len(self.word)]
        self.num_letters = word.__sizeof__
        self.num_lives = num_lives
        self.word_list = ["papayas","bananas","grapes","strawberries", "avocado"]
        self.list_of_guesses = []

# check_guess method that will ask the user to guess a letter and another method that will check if the guess is in the word.
    def check_guess_method(self, guess):
        if len(guess) ==1 and guess in ascii_lowercase:
            print ("Good guess! {} is in the word.".format(guess))
            for i in range (len(self.word)):
                if guess == self.word[i]:
                    self.word_guessed = self.word_guessed + [i]
                    print(self.word_guessed)
                #self.word_guessed = ''.join(self.word_guessed)
        else:
            self.num_lives = self.num_lives - 1
            print ("Sorry, {} is not in the word.".format(guess))
            print ("You have {} lives left.".format(self.num_lives))
    
        self.list_of_guesses.append(guess)    
    
    def ask_for_input (self):
        while True:
            guess = input ("guess a letter ")
            if guess not in ascii_lowercase:
                print ("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                    print ("You already tried that letter!")
            else :
                self.check_guess_method(guess)
                self.list_of_guesses.append(guess)


#Hangman.ask_for_input(word_list)

game = Hangman(word_list)
game.ask_for_input()



