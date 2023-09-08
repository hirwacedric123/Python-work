import random
import string
""" GROUP MEMBERS:

    Names:-HIRWA CYUZUZO Cedric     223013417
          -NIYONIZERA Deborah       223013745
          -RUKUNDO Wilson           223004931
"""


word_list_custom = ["programming", "computer", "challenge", "python", "developer", "hangman", "gaming"]

# Function to choose a random word from the custom list
def select_random_word():
    return random.choice(word_list_custom)

# Function to play the custom Hangman game
def play_custom_hangman():
    print("Welcome to the Custom Hangman Game!")
    secret_word_custom = select_random_word()
    guessed_chars = set()
    remaining_attempts = 6
    remaining_warnings = 3

    while remaining_attempts > 0:
        print("\nAttempts left: {}".format(remaining_attempts))
        print("Available letters:", "".join(sorted(set(string.ascii_lowercase) - guessed_chars)))
        
        word_display = ""
        for letter in secret_word_custom:
            if letter in guessed_chars:
                word_display += letter
            else:
                word_display += "-"

        print("Word:", word_display)

        user_input = input("Guess a letter or the whole word: ").lower()

        if len(user_input) == 1 and user_input in string.ascii_lowercase:
            if user_input in guessed_chars:
                if remaining_warnings > 0:
                    remaining_warnings -= 1
                    print("You've already guessed that letter. Warnings left: {}".format(remaining_warnings))
                else:
                    remaining_attempts -= 1
                    print("You've already guessed that letter. No warnings left. You lose an attempt.")
            else:
                guessed_chars.add(user_input)
                if user_input in secret_word_custom:
                    print("Good guess!")
                else:
                    remaining_attempts -= 2 if user_input in "aeiou" else 1
                    print("Oops! That letter is not in the word.")
        elif len(user_input) == len(secret_word_custom) and user_input.isalpha():
            if user_input == secret_word_custom:
                print("Congratulations, you've won! The word is:", secret_word_custom)
                break
            else:
                remaining_attempts -= 1
                print("Sorry, that's not the correct word.")
        else:
            if remaining_warnings > 0:
                remaining_warnings -= 1
                print("Invalid input. Warnings left: {}".format(remaining_warnings))
            else:
                remaining_attempts -= 1
                print("Invalid input. No warnings left. You lose an attempt.")

        # Check if the player has guessed the entire word
        if word_display == secret_word_custom:
            print("Congratulations, you've won! The word is:", secret_word_custom)
            break

    if remaining_attempts <= 0:
        print("Sorry, you've run out of attempts. The word was:", secret_word_custom)

# Start the custom game
play_custom_hangman()
