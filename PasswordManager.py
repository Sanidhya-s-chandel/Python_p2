import os
import json
import base64
from cryptography.fernet import Fernet
import random
import string

class PasswordManager:
    def __init__(self, master_key):
        self.master_key = master_key
        self.data_file = "passwords.json"
        self.key = self._derive_key(master_key)
        self.fernet = Fernet(self.key)
        self.passwords = self._load_passwords()

    def _derive_key(self, master_key):
        # Derive a 32-byte key from the master key
        return base64.urlsafe_b64encode(master_key.zfill(32).encode())

    def _load_passwords(self):
        if not os.path.exists(self.data_file):
            return {}
        with open(self.data_file, "r") as file:
            encrypted_data = file.read()
            if not encrypted_data:
                return {}
            decrypted_data = self.fernet.decrypt(encrypted_data.encode()).decode()
            return json.loads(decrypted_data)

    def _save_passwords(self):
        encrypted_data = self.fernet.encrypt(json.dumps(self.passwords).encode()).decode()
        with open(self.data_file, "w") as file:
            file.write(encrypted_data)

    def generate_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    def add_password(self, category, service, username, password=None):
        if password is None:
            password = self.generate_password()
        if category not in self.passwords:
            self.passwords[category] = {}
        self.passwords[category][service] = {
            "username": username,
            "password": password
        }
        self._save_passwords()
        return password

    def get_password(self, category, service):
        if category in self.passwords and service in self.passwords[category]:
            return self.passwords[category][service]
        return None

    def search_service(self, keyword):
        results = []
        for category, services in self.passwords.items():
            for service, details in services.items():
                if keyword.lower() in service.lower():
                    results.append((category, service, details))
        return results

    def list_categories(self):
        return list(self.passwords.keys())

    def list_services(self, category):
        if category in self.passwords:
            return list(self.passwords[category].keys())
        return []

# CLI Interface
def main():
    print("Welcome to the Password Manager!")
    master_key = input("Enter your master key: ")
    manager = PasswordManager(master_key)

    while True:
        print("\nOptions:")
        print("1. Add a new password")
        print("2. Retrieve a password")
        print("3. Generate a strong password")
        print("4. Search for a service")
        print("5. List categories")
        print("6. Exit")
        
        choice = input("Select an option: ")

        if choice == "1":
            category = input("Enter the category: ")
            service = input("Enter the service name: ")
            username = input("Enter the username: ")
            password = input("Enter a password (leave blank to generate one): ") or None
            new_password = manager.add_password(category, service, username, password)
            print(f"Password added for {service}. Generated password: {new_password}")

        elif choice == "2":
            category = input("Enter the category: ")
            service = input("Enter the service name: ")
            details = manager.get_password(category, service)
            if details:
                print(f"Username: {details['username']}, Password: {details['password']}")
            else:
                print("Service not found.")

        elif choice == "3":
            length = int(input("Enter the length of the password: "))
            print("Generated password:", manager.generate_password(length))

        elif choice == "4":
            keyword = input("Enter a keyword to search for: ")
            results = manager.search_service(keyword)
            if results:
                for category, service, details in results:
                    print(f"Category: {category}, Service: {service}, Username: {details['username']}")
            else:
                print("No matching services found.")

        elif choice == "5":
            categories = manager.list_categories()
            print("Categories:", ", ".join(categories))

        elif choice == "6":
            print("Exiting Password Manager. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()