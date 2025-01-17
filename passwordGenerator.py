import random
import string

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_special=True):
    """
    Generate a secure password with the specified options.

    Parameters:
        length (int): Length of the password (default is 12).
        include_uppercase (bool): Whether to include uppercase letters (default is True).
        include_numbers (bool): Whether to include numbers (default is True).
        include_special (bool): Whether to include special characters (default is True).

    Returns:
        str: The generated password.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")
    
    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ""
    numbers = string.digits if include_numbers else ""
    special = string.punctuation if include_special else ""

    # Ensure the password contains at least one character from each selected pool
    pools = [lowercase]
    if include_uppercase:
        pools.append(uppercase)
    if include_numbers:
        pools.append(numbers)
    if include_special:
        pools.append(special)

    # Build the password
    all_characters = "".join(pools)
    if not all_characters:
        raise ValueError("No character pools selected.")
    
    password = [
        random.choice(pool) for pool in pools
    ]
    password += random.choices(all_characters, k=length - len(password))
    random.shuffle(password)
    
    return "".join(password)

# Example usage
if __name__ == "__main__":
    length = int(input("Enter the password length: "))
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes"
    include_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
    include_special = input("Include special characters? (yes/no): ").strip().lower() == "yes"

    password = generate_password(length, include_uppercase, include_numbers, include_special)
    print("Generated Password:", password)