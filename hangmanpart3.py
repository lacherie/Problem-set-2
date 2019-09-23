# Problem Set 2, hangman.py
# Name: lacherie
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
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
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()
  

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    answer = True
    for char in secret_word:
        if char in letters_guessed:
            answer = True
        else:
            answer = False
            break
    return(answer)   


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''    
    guessed_word_list = []
    # replace every char with a "_ "
    for char in secret_word:
        if char in letters_guessed:
            guessed_word_list.append(char)
        else:
            guessed_word_list.append("_ ")
            # replace letter in secret word with "_ "
    guessed_word_str = ''.join(guessed_word_list)
    # turn list back to string        
    return(guessed_word_str)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters_left_str = "abcdefghijklmnopqrstuvwxyz"
    letters_left_list = list(letters_left_str)
    for char in letters_guessed:
        letters_left_list.remove(char)
    letters_left_str = ''.join(letters_left_list)
    return(letters_left_str)


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word_no_spaces = my_word.replace(" ","")
    if len(my_word_no_spaces) != len(other_word):
        answer = False
        return(answer)
    for i in range(len(my_word_no_spaces)):
        if my_word_no_spaces[i] == other_word[i]:
            answer = True
        elif my_word_no_spaces[i] == "_" and other_word[i] not in my_word_no_spaces:
            answer = True
            # exclude words that have an already guessed letter in a gap
        else:
            answer = False
            break
    return(answer)



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''

    for word in wordlist:
        if match_with_gaps(my_word, word) == True:
            print(word)




def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    vowels = ["a","e","i","o","u"]
    consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is ",len(secret_word),"letters long.")
    print("You have ", warnings_remaining, "warnings left.")
    print("-------------")
    while guesses_remaining > 0:
        if is_word_guessed(secret_word,letters_guessed) == False:
            print("You have ",guesses_remaining," guesses left.")
            print("Available letters: ",get_available_letters(letters_guessed))
            letter_input = input(str("Please guess a letter: "))
            if letter_input.isupper():
                letter_input = letter_input.lower()
                # turn all uppercase letters into lower case ones to accept both
            if letter_input in consonants or letter_input in vowels:
            # don't add special characters to letters_guessed
                if letter_input not in letters_guessed:
                    letters_guessed.append(letter_input)
                    guessed_word_str = get_guessed_word(secret_word,letters_guessed)
                    if letter_input in secret_word:
                        print("Good guess: " + guessed_word_str)
                    else:
                        if letter_input in vowels:                        
                            guesses_remaining -= 2
                        else:
                            guesses_remaining -= 1
                        print("Oops! That letter is not in my word: ",guessed_word_str)
                else:
                    if warnings_remaining > 0:
                        warnings_remaining -= 1
                        print("Oops! You've already guessed that letter. You have",warnings_remaining,"warnings left: ",guessed_word_str)
                    else:
                        guesses_remaining -= 1
                        print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: ",guessed_word_str)
            elif(letter_input == "*"):
                show_possible_matches(guessed_word_str)
            else:
                guessed_word_str = get_guessed_word(secret_word,letters_guessed)
                #if you entered only special characters from the start, there is no guessed_word_str
                if warnings_remaining > 0:
                    warnings_remaining -= 1
                    print("Oops! That is not a valid letter. You have",warnings_remaining,"warnings left.")
                else:
                    guesses_remaining -= 1
                    print("Oops! That is not a valid letter. You have no warnings left so you lose one guess: ",guessed_word_str)
            print("-------------")
        else:
            score = len(set(secret_word)) * guesses_remaining
            # calculate score: number of unique characters times guesses left
            print("Congratulations, you won!")
            print("Your total score for this game is: ", score)
            break
    if guesses_remaining <= 0:
        print("Sorry, you ran out of guesses. The word was",secret_word+".")



if __name__ == "__main__":

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
