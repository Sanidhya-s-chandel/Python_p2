class BankAccount:
    def __init__(self, account_number, name, balance=0):
        """
        Initialize a new bank account with account number, owner name, and optional initial balance.
        """
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit money into the account.
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw money from the account if sufficient funds are available.
        """
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def get_balance(self):
        """
        Check the current balance of the account.
        """
        print(f"Account Balance: {self.balance}")
        return self.balance

    def display_details(self):
        """
        Display account details.
        """
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Account Balance: {self.balance}")


# Main program to use the banking system
def main():
    print("Welcome to the Banking System!")
    accounts = {}

    while True:
        print("\n1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Display Account Details")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            account_number = input("Enter a new account number: ")
            name = input("Enter the account holder's name: ")
            initial_deposit = float(input("Enter the initial deposit amount (or 0): "))
            accounts[account_number] = BankAccount(account_number, name, initial_deposit)
            print("Account created successfully!")

        elif choice == '2':
            account_number = input("Enter your account number: ")
            if account_number in accounts:
                amount = float(input("Enter amount to deposit: "))
                accounts[account_number].deposit(amount)
            else:
                print("Account not found!")

        elif choice == '3':
            account_number = input("Enter your account number: ")
            if account_number in accounts:
                amount = float(input("Enter amount to withdraw: "))
                accounts[account_number].withdraw(amount)
            else:
                print("Account not found!")

        elif choice == '4':
            account_number = input("Enter your account number: ")
            if account_number in accounts:
                accounts[account_number].get_balance()
            else:
                print("Account not found!")

        elif choice == '5':
            account_number = input("Enter your account number: ")
            if account_number in accounts:
                accounts[account_number].display_details()
            else:
                print("Account not found!")

        elif choice == '6':
            print("Thank you for using the Banking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the banking system
if __name__ == "__main__":
    main()