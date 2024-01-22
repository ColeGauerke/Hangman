# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random


WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    return all(char in letters_guessed for char in secret_word)




def get_guessed_word(secret_word, letters_guessed):
    word_with_spaces = ""
    secret_word_list = list(secret_word)
    emptyList = ["__"] * len(secret_word_list)
    for c in range(len(secret_word_list)):
        for a in letters_guessed:
            if a == secret_word_list[c]:
                emptyList[c] = a
    word_with_spaces = " ".join(emptyList)
    return word_with_spaces



def get_available_letters(letters_guessed):
    avletters = " ".join(letters_guessed)
    return avletters
    
    

def hangman(secret_word):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    guesses = []
    solved = False
    secretWordList = list(secret_word)
    numGuesses = 6
    warnings = 2
    wordLength = len(secret_word)
    print("The secret word is",wordLength,"characters long")
    while solved == False and warnings >= 0:
        print("The Available letters are:"," ".join(letters))
        print("You have",numGuesses,"lives remaining")
        guess = str(input("Please Guess a Letter: "))
        if guess in letters and numGuesses >= 0:
            guesses.append(guess)
            letters.remove(guess)
            if guess in secretWordList:
                print("Great Guess "+guess+" is in my word: ", get_guessed_word(secret_word, guesses))
                solved = is_word_guessed(secret_word, guesses)
                if solved == True:
                    break 
            else:
                numGuesses -= 1
                print(get_guessed_word(secret_word, guesses))
                print("Oops! That letter is not in my word, try again ")
        elif guess not in letters and warnings >= 0:
            warnings -= 1
            if warnings >= 0:
                print("Invalid Guess, that character is not a valid letter! You have",warnings,"warnigns left!")
        elif guess in guesses and warnings > 0:
            warnings -= 1
            if warnings >= 0:
                print("You alrady guessed that letter! You have",warnings,"warnings left")
        #elif numGuesses == 1:
        print("===================")
        if numGuesses == 0:
            break
    
    
    if solved == True:
        print("Congratulations, You Won!")
    else:
        print("Womp Womp, YOU LOST :(")
        print("The Correct Word Was: "+secret_word)
    pass

hangman(choose_word(wordlist))

