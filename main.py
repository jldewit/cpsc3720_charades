import functions

words = [] 
#holds the list of words the user has added to the game
rounds = input("how many rounds would you like to play? (type a number) ")
#holds the number of rounds the game will run
print("you entered ",rounds)
keepAdd = True
while(keepAdd):
    add = input("would you like to add a word to the list? (Y/N) ")
    if(add == 'Y')or(add == 'y'):
        words.append(input("enter the word you would like to add to the list "))
    else:
        if(len(words) == 0):
            print("there are no words in the list, please add a word ")
    while((add!='N') and (add!='n')):
        add = input("would you like to add a word to the list? (Y/N) ")
        if(add == 'Y')or(add == 'y'):
            words.append(input("enter the word you would like to add to the list "))
        else:
            if(len(words) == 0):
                print("there are no words in the list, please add a word ")
            else:
                keepAdd = False
print("the game will draw from the following words: ")
for x in range(len(words)):
    print(words[x])
while(rounds>0 and len(words)>0):
    words = functions.shuffle(words)
    current_word = functions.draw(words)
    words.remove(current_word)
#pass