import os
import random
import SpellChecker

spell = SpellChecker()

#TODO
#takes a string as a parameter
#uses the SpellChecker api to run a spell check on the word
#returns 
def spellcheck(word):
    misspelled = spell.unknown([word])
    for i in misspelled:
            if (spell.correction(word) != word)
                return false
            else 
                return true
    
#TODO
#takes a list of strings as a parameter
#randomly selects a string from the list
#returns the randomly selected string
def draw(words):
    pass

#TODO
#takes a list of strings as a parmeter
#returns the shuffled list
def shuffle(words):
    pass
