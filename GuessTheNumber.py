import random

class NumberGuessingGame:
    def __init__(self, min_number, max_number, max_attempts):
        self.min_number = min_number
        self.max_number = max_number
        self.max_attempts = max_attempts
        self.secret_number = random.randint(self.min_number, self.max_number)
        self.attempts = 0
        self.is_game_over = False

    def get_player_guess(self):
        while True:
            try:
                guess = int(input(f"Enter your guess ({self.min_number} - {self.max_number}): "))
                if guess < self.min_number or guess > self.max_number:
                    raise ValueError("Guess is out of bounds!")
                return guess
            except ValueError as ve:
                print(f"Invalid input: {ve}. Please try again.")

    def check_guess(self, guess):
        self.attempts += 1
        if guess == self.secret_number:
            self.is_game_over = True
            return "Correct! You've guessed the number."
        elif guess < self.secret_number:
            return "Too low!"
        else:
            return "Too high!"

    def play(self):
        print(f"Welcome to the Number Guessing Game! You have {self.max_attempts} attempts.")
        print(f"Guess the number between {self.min_number} and {self.max_number}.")
        
        while not self.is_game_over and self.attempts < self.max_attempts:
            guess = self.get_player_guess()
            result = self.check_guess(guess)
            print(result)
            
            if self.is_game_over:
                print(f"Congratulations! You guessed the number in {self.attempts} attempts.")
                break
        else:
            print(f"Game over! The correct number was {self.secret_number}.")

if __name__ == "__main__":
    game = NumberGuessingGame(min_number=1, max_number=100, max_attempts=7)
    game.play()