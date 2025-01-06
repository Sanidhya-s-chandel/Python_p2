import random

class Hangman:
    def __init__(self, word_list, max_attempts=6):
        """
        Initialize the Hangman game with a list of words and maximum attempts.
        """
        self.word_list = word_list
        self.max_attempts = max_attempts
        self.word_to_guess = random.choice(self.word_list).lower()
        self.guessed_word = ["_"] * len(self.word_to_guess)
        self.attempts_left = self.max_attempts
        self.guessed_letters = set()

    def display_progress(self):
        """
        Display the current state of the guessed word and remaining attempts.
        """
        print("\nCurrent Word: " + " ".join(self.guessed_word))
        print(f"Attempts Remaining: {self.attempts_left}")
        print(f"Guessed Letters: {', '.join(sorted(self.guessed_letters)) if self.guessed_letters else 'None'}")

    def guess_letter(self, letter):
        """
        Process a player's guess and update the game state.
        """
        letter = letter.lower()

        if not letter.isalpha() or len(letter) != 1:
            print("Invalid input. Please enter a single alphabetical character.")
            return

        if letter in self.guessed_letters:
            print(f"You've already guessed the letter '{letter}'. Try another one.")
            return

        self.guessed_letters.add(letter)

        if letter in self.word_to_guess:
            print(f"Good job! The letter '{letter}' is in the word.")
            for index, char in enumerate(self.word_to_guess):
                if char == letter:
                    self.guessed_word[index] = letter
        else:
            self.attempts_left -= 1
            print(f"Oops! The letter '{letter}' is not in the word.")

    def is_game_over(self):
        """
        Check if the game is over (win or lose).
        """
        return self.attempts_left == 0 or "_" not in self.guessed_word

    def is_winner(self):
        """
        Check if the player has won the game.
        """
        return "_" not in self.guessed_word

    def play(self):
        """
        Main game loop to play the Hangman game.
        """
        print("Welcome to the Hangman Game!")
        print("Try to guess the word, one letter at a time.")
        print(f"You have {self.max_attempts} attempts. Good luck!")

        while not self.is_game_over():
            self.display_progress()
            guess = input("Enter a letter: ")
            self.guess_letter(guess)

        self.display_progress()

        if self.is_winner():
            print("\nCongratulations! You guessed the word:", self.word_to_guess)
        else:
            print("\nGame over! The word was:", self.word_to_guess)


# Main program to run the Hangman game
if __name__ == "__main__":
    words = ["python", "developer", "hangman", "programming", "software", "keyboard", "algorithm"]
    hangman_game = Hangman(word_list=words)
    hangman_game.play()