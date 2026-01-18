# hangman_lib.py
import random

WORDS = ["python", "hangman", "programming", "science", "college", "astronomy"]

HANGMAN_PICS = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

def get_random_word():
    """Return a random word from WORDS list."""
    return random.choice(WORDS)

def print_hangman_image(mistakes):
    """Print the hangman ASCII art based on mistakes made."""
    print(HANGMAN_PICS[mistakes])

## Constants ##
MAX_MISTAKES = 6

## State variables ##
secret_word = get_random_word()     # from hangman_lib
letters_guessed = []                # no letters guessed initially
mistakes_made = 0

## Helper functions ##
def word_guessed():
    """Returns True iff the player has successfully guessed the word."""
    return all(letter in letters_guessed for letter in secret_word)

def print_guessed():
    """Returns a string of the word with not-guessed letters as dashes."""
    return ''.join([letter if letter in letters_guessed else '-' for letter in secret_word])

## Main game code ##
print("Welcome to Hangman!\n")

first_time = input("Is this your first time playing Hangman? (y/n) ").lower()
print()

if first_time == "y":
    print("The objective of Hangman is to guess a secret word letter by letter.")
    print("If you guess a letter in the word, we'll show you that letter.")
    print("But if you guess wrong, we'll draw part of the hangman's body.")
    print("Don't let his whole body get drawn, or else you lose!\n")

print("Great, so you're ready to play. Just two things that might help:")
print(f"1) The secret word has {len(secret_word)} letters.")
print(f"2) It takes {MAX_MISTAKES} wrong guesses to lose.\n")
print("Good luck!\n")
input("[Press enter when ready to play.]")

print_hangman_image(0)
print()

# Main game loop
while mistakes_made < MAX_MISTAKES:
    print("\nThe word so far:", print_guessed())
    print("Letters guessed so far:", ' '.join(letters_guessed))
    print("Wrong guesses remaining:", MAX_MISTAKES - mistakes_made, "\n")

    guess = input("What letter will you guess? ").lower()

    if guess == "":
        print("You have to guess something...")
    elif len(guess) > 1:
        print("You can only guess one letter at a time!")
    elif not guess.isalpha():
        print("You can only guess letters, not numbers or symbols!")
    elif guess in letters_guessed:
        print("You've already guessed this letter!")
    else:
        letters_guessed.append(guess)
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
            if word_guessed():
                print("In fact, that's the last letter!")
                break
        else:
            mistakes_made += 1
            print(f"Sorry, no luck. '{guess}' is not in the word.\n")
            print_hangman_image(mistakes_made)
            print()

# End of game
print()
if mistakes_made >= MAX_MISTAKES:
    print("Oh no, you guessed wrong too many times! You lose.")
    print(f'The word was "{secret_word}".\n')
    print("GAME OVER")
else:
    print("Congratulations... you win!")
    print(f'You correctly guessed the word "{secret_word}".')
