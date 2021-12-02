import os
import random
from spellchecker import SpellChecker

spell = SpellChecker()

#TODO
#takes a string as a parameter
#uses the SpellChecker api to run a spell check on the word
#returns 
def spellcheck(word):
    if (spell.correction(word) != word):
        return False
    else: 
        return True
    
#TODO
#takes a list of strings as a parameter
#randomly selects a string from the list
#returns the randomly selected string
def draw(words):
    l = len(words)
    r = random.randint(0, l-1)
    return words[r]


#TODO
#takes a list of strings as a parmeter
#returns the shuffled list
def shuffle(words):
    random.shuffle(words)
    return words
