# Import choice to select a secret word from a list of words
from random import choice
import sys

# Create a class of colors to color the letters if needed
class colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

# ---------- Functions to make the list and select a secret word. ---------- #

def make_list(nb_letters):
    """Makes the list of words.
    Args:
        nb_letters (int): number of letters in the words of the list
    Returns:
        list: the list of words
    """
    words_list = []
    # Open the file that contains the words with the required number of letters
    with open(f'data/mots_{nb_letters}.txt', 'r') as file:
        for word in file:
            # For each word in the file, we remove "\n" and add it to the list
            words_list.append(word.replace("\n",""))
    return words_list

def make_bigger_list(nb_letters):
    """Make a bigger list of words from several other lists.
    Args:
        nb_letters (int): the maximum number of letters in the words
    Returns:
        list: the list of words
    """
    assert nb_letters>3, 'wrong number'
    words_list = []
    # In the data folder, there are lists of 4 letter words to 12 letter.
    # Go from 4 to the maximum number of letters and add each list to the
    # bigger one.
    for number in range(4,nb_letters+1):
        words_list += make_list(number)
    return words_list

def get_random_word(words_list):
    """Randomly choose a word from a list of words.
    Args:
        words_list (list): the list of words
    Returns:
        str: a random word from the list
    """
    # Use the function choice from the library random
    return choice(words_list)

# -------------------------------------------------------------------------- #

# -------------------------- Functions for inputs -------------------------- #
def welcome():
    """Function for printing the welcome text, make the list and select a secret
    word from it depending of how many letters the user chooses.
    Returns:
        list: the list of words
        str: the secret word
    """
    print("\nBienvenue dans ma version de Wordle !\n")
    print("Choississez la taille du mot mystère (entre 4 et 12). Entrez quit pour quitter.\n")
    nb_letters = ""
    # This conditions allow the player to quit
    while nb_letters!='quit' or nb_letters!='quitter':
        nb_letters = str(input())
        # The method isdigit() returns whether or not the input is a number
        if nb_letters.isdigit():
            nb_letters = int(nb_letters)
            # The length of the word cannot be less than 4 or more than 12
            if nb_letters>3 and nb_letters<13:
                print(f"Vous avez choisi un mot de {nb_letters} lettres.\n")
                break
            else:
                print("Entrez un nombre entre 4 et 12 (compris).\n")
        else:
            print("Saisie invalide. Veuillez réessayer.\n")
    words_list = make_list(nb_letters)
    secret_word = get_random_word(words_list)
    return words_list, secret_word

def valid_length_word(word, words_list):
    """Function to test the validity of the length of the input word.
    Args:
        word (str): input word
        words_list (list): list of words whose size must be the same as the word entered
    Returns:
        bool: whether or not the length of the word is valid
    """
    if len(word)==len(words_list[-1]):
        return True
    else:
        return False

def valid_dictionary_word(word, words_list):
    """Function to check if the word is in the dictionary.
    Args:
        word (str): word to test
        words_list (list): the "dictionary"
    Returns:
        bool: wether or not the word is in the dictionary
    """
    if word in words_list:
        return True
    else:
        return False

def user_input(words_list, word_to_guess):
    """Function to do each input from the user.
    Args:
        words_list (list): the list of words
    Returns:
        str: the input word, if it's correct
    """
    word = ""
    # Allows the user to quit whenever they want by entering 'quit' or 'quitter'
    while 1:
        word = str(input().lower())
        if word=='quit' or word=='quitter':
            return word
        error = False
        # Removes the user input for more visibility
        if error:
            sys.stdout.write(u"\u001b[2F\u001b[2K\u001b[2E")
        else:
            sys.stdout.write(u"\u001b[1F\u001b[2K\u001b[1F\u001b[2K")
        # Checks the validity of its length
        if valid_length_word(word,words_list):
            # Checks the if the word is in the dictionary
            if valid_dictionary_word(word,words_list):
                # So, if the word passes these tests, returns it
                return word
            else:
                print("Votre mot n'est pas dans le dictionnaire.")
                print(word_to_guess)
                error = True
        else:
            print("Votre mot n'est pas de la bonne longueur.")
            print(word_to_guess)
            error = True

def colored(letter, color):
    """Function to get the letter colored as we want.
    Args:
        letter (str): the letter we want to color
        color (str): the color we want for the letter
    Returns:
        str: the colored letter
    """
    # In wordle, there are only two variations of color, green and yellow.
    if color=="green":
        return colors.GREEN + letter + colors.RESET
    elif color=="yellow":
        return colors.YELLOW + letter + colors.RESET

def letters_dict(word):
    """Function to put in a dictionary how many times a letter appears in the word.
    Args:
        word (str): the word we want to class
    Returns:
        dict: the dictionary that contains how many times each letter appears
        in the word
    """
    dictio = {}
    for letter in word:
        # If the letter is already in the dictionary, adds 1 to its value
        if letter in dictio.keys():
            dictio[letter] += 1
        # If not, add the letter as a new key and 1 as its value
        else:
            dictio[letter] = 1
    return dictio

def display_word(word, secret_word, word_to_guess):
    """Function to edit the word to display and the word to guess (word to display
    is the test word with its colored letter and the word to guess is the word
    with spaces in it, for each missing letter).
    Args:
        word (str): the input word
        secret_word (str): the secret word that the user have to find
        word_to_guess (str): the word with spaces for each missing letter
    Returns:
        str: the word to guess, to update it at each try
    """
    word_to_display = ""
    indexes = []
    # We need to do the dictio at each input because we need to edit it for 
    # each test word. It will be needed to not display several yellow letter
    # when there should be only one.
    dictio = letters_dict(secret_word)
    # For each letter in the word
    for letter_index in range(len(word)):
        word_letter = word[letter_index]
        # If the letter is the same at the same place in the secret_word
        if word_letter==secret_word[letter_index]:
            # Colors the letter in green
            word_to_display += colored(word_letter, "green")
            # Adds the index to a list
            indexes.append(letter_index)
        # If the letter is not the same at the same place in the secret word
        # but is in the word anyway
        elif word_letter in secret_word:
            if dictio[word_letter]>0:
                # Colors the letter in yellow and substract 1 to the dictionary
                # of letters, if it's not 0
                word_to_display += colored(word_letter, "yellow")
                dictio[word_letter] -= 1
            else:
                # If there's 0 for the letter in the dictionary, it's because we
                # already encountered them all, so we don't color it
                word_to_display += word_letter
        else:
            word_to_display += word_letter
    # Transforms the word to guess as a list, within each letter is one element
    word_to_guess_list = list(word_to_guess)
    for index in range(len(secret_word)):
        if index in indexes:
            # If the user have found a letter, replaces the space (_) by it
            word_to_guess_list[index] = secret_word[index]
    # Reforms the word
    word_to_guess = "".join(word_to_guess_list)
    return word_to_display, word_to_guess

def run():
    # Gets the words list and the secret word with welcome()
    words_list, secret_word = welcome()
    # print(secret_word)
    # Creates the word_to_guess, with the first letter of the secret word and
    # spaces formed by underscores.
    word_to_guess = secret_word[0]+"_"*(len(secret_word)-1)
    print(word_to_guess)
    word_found = False
    counter = 0
    while not word_found:
        # Gets the word tests with user_input()
        word_test= user_input(words_list, word_to_guess)
        counter += 1
        if word_test=='quit' or word_test=='quitter':
            print(f"Le mot secret était {secret_word}. Merci d'avoir joué !")
            break
        if counter>5:
            print(f"Vous avez fait 6 essais infructueux, le mot secret \
était {secret_word}. Merci d'avoir joué !")
            break
        # Gets word_to_display and word_to_guess with display_word()
        word_to_display, word_to_guess = display_word(word_test,
                                                      secret_word,
                                                      word_to_guess)
        print(word_to_display)
        if word_test==secret_word:
            # If the input word is the secret word, the word is found, so
            # we put word_found as True so the loop stops. We don't have to
            # print word_to_guess.
            word_found = True
        else:
            # Otherwise, we print word_to_guess
            print(word_to_guess)
    else:
        print(f"Félicitations ! Le mot était bien {secret_word} !")


run()