import random

def generate_username():
    adjectives = ["Cool", "Swift", "Epic", "Funky", "Chill", "Witty", "Brave", "Snazzy", "Zesty", "Nifty"]
    nouns = ["Panther", "Falcon", "Ninja", "Wizard", "Vortex", "Shadow", "Rider", "Titan", "Phoenix", "Blaze"]
    number = random.randint(100, 999)
    
    username = f"{random.choice(adjectives)}{random.choice(nouns)}{number}"
    return username

if __name__ == "__main__":
    print("Your unique username is:", generate_username())