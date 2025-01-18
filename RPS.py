import random

def get_computer_choice(choices):
    return random.choice(choices)

def determine_winner(user_choice, computer_choice, rules):
    if user_choice == computer_choice:
        return "tie"
    elif computer_choice in rules[user_choice]:
        return "win"
    else:
        return "lose"

def display_rules(rules):
    print("\nRules of the game:")
    for choice, defeats in rules.items():
        print(f"{choice.capitalize()} beats {', '.join(defeats).capitalize()}.")

def play_game():
    print("Welcome to the Advanced Rock, Paper, Scissors Game!")
    print("Choose your mode:")
    print("1. Classic (Rock, Paper, Scissors)")
    print("2. Advanced (Rock, Paper, Scissors, Lizard, Spock)")
    
    mode = input("Enter 1 or 2: ")
    if mode == "1":
        choices = ["rock", "paper", "scissors"]
        rules = {
            "rock": ["scissors"],
            "paper": ["rock"],
            "scissors": ["paper"]
        }
    elif mode == "2":
        choices = ["rock", "paper", "scissors", "lizard", "spock"]
        rules = {
            "rock": ["scissors", "lizard"],
            "paper": ["rock", "spock"],
            "scissors": ["paper", "lizard"],
            "lizard": ["spock", "paper"],
            "spock": ["scissors", "rock"]
        }
    else:
        print("Invalid mode. Exiting the game.")
        return
    
    display_rules(rules)
    print("\nType 'quit' to exit the game.")
    
    user_score = 0
    computer_score = 0
    round_number = 0

    while True:
        round_number += 1
        print(f"\n--- Round {round_number} ---")
        print(f"Your score: {user_score} | Computer score: {computer_score}")
        
        user_choice = input(f"Choose ({', '.join(choices)}): ").lower()
        if user_choice == "quit":
            print("Thanks for playing!")
            break
        elif user_choice not in choices:
            print("Invalid choice. Please try again.")
            round_number -= 1
            continue
        
        computer_choice = get_computer_choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice, rules)
        if result == "tie":
            print("It's a tie!")
        elif result == "win":
            print("You win this round!")
            user_score += 1
        else:
            print("You lose this round!")
            computer_score += 1
        
        if user_score == 5:
            print("\nCongratulations! You won the game!")
            break
        elif computer_score == 5:
            print("\nGame over! The computer won!")
            break

# Run the game
play_game()