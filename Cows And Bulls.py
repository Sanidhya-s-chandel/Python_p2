import random
import time

def generate_secret_code(length=4):
    """Generate a secret code with unique digits."""
    digits = list("0123456789")
    random.shuffle(digits)
    return "".join(digits[:length])

def get_feedback(secret, guess):
    """Calculate the number of cows and bulls based on the guess."""
    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    cows = sum(1 for g in guess if g in secret) - bulls
    return bulls, cows

def display_intro():
    """Display the game introduction."""
    print("""\
==================== COWS AND BULLS ====================
Welcome to the Cows and Bulls game! Here's how to play:
1. The computer will generate a secret code of unique digits.
2. Your goal is to guess the secret code.
3. After each guess, you'll get feedback:
   - Bulls: Correct digit in the correct position.
   - Cows: Correct digit in the wrong position.
4. Keep guessing until you crack the code!
5. You can type 'hint' for a hint or 'exit' to quit the game.
========================================================
""")

def provide_hint(secret, revealed):
    """Provide a hint by revealing one unrevealed digit."""
    unrevealed = [s for i, s in enumerate(secret) if not revealed[i]]
    if unrevealed:
        hint = random.choice(unrevealed)
        revealed[secret.index(hint)] = True
        return hint
    return None

def play_game():
    """Main game loop."""
    display_intro()

    length = 4
    secret_code = generate_secret_code(length)
    attempts = 0
    revealed = [False] * length

    print(f"The secret code is a {length}-digit number with unique digits. Good luck!")

    while True:
        guess = input("\nEnter your guess: ").strip()
        attempts += 1

        # Check for special commands
        if guess.lower() == "hint":
            hint = provide_hint(secret_code, revealed)
            if hint:
                print(f"Hint: One of the digits in the code is '{hint}'.")
            else:
                print("No more hints available! All digits have been revealed.")
            continue

        if guess.lower() == "exit":
            print("Thanks for playing! The secret code was:", secret_code)
            break

        # Validate guess
        if len(guess) != length or not guess.isdigit() or len(set(guess)) != len(guess):
            print(f"Invalid guess! Please enter a {length}-digit number with unique digits.")
            continue

        # Get feedback
        bulls, cows = get_feedback(secret_code, guess)
        print(f"Feedback: {bulls} Bulls, {cows} Cows")

        # Check for win
        if bulls == length:
            print(f"\nCongratulations! You cracked the code {secret_code} in {attempts} attempts!")
            break

if __name__ == "__main__":
    play_game()