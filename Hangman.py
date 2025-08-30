08.30 10:39 AM
import random

# List of words to guess
words = ["python", "hangman", "programming", "developer", "computer", "algorithm"]

# Choose a random word
word = random.choice(words)
word_letters = set(word)  # Unique letters in the word
guessed_letters = set()   # Correct guesses
wrong_letters = set()     # Wrong guesses
lives = 6                 # Number of chances

print("=== Welcome to Hangman! ===")

while len(word_letters) > 0 and lives > 0:
    # Show current status
    print("\nYou have", lives, "lives left.")
    print("Wrong guesses:", " ".join(sorted(wrong_letters)))

    # Display the word with guessed letters
    word_display = [letter if letter in guessed_letters else "_" for letter in word]
    print("Word:", " ".join(word_display))

    # Take user guess
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue

    if guess in guessed_letters or guess in wrong_letters:
        print("You already guessed that letter.")
        continue

    # Check guess
    if guess in word_letters:
        guessed_letters.add(guess)
        word_letters.remove(guess)
        print("✅ Correct!")
    else:
        wrong_letters.add(guess)
        lives -= 1
        print("❌ Wrong!")

# Game over conditions
if lives == 0:
    print("\n You lost! The word was:", word)
else:
    print("\n Congratulations! You guessed the word:", word)
