import requests

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"
        self.rates = {}

    def fetch_exchange_rates(self, base_currency):
        """Fetch exchange rates for the base currency from the API."""
        try:
            response = requests.get(self.api_url + base_currency)
            if response.status_code == 200:
                data = response.json()
                self.rates = data['conversion_rates']
                print(f"Exchange rates for {base_currency} fetched successfully!")
            else:
                print("Error fetching exchange rates. Check your API key or base currency.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def convert_currency(self, from_currency, to_currency, amount):
        """Convert currency from one to another based on the fetched exchange rates."""
        if not self.rates:
            print("Exchange rates not available. Please fetch them first.")
            return None
        
        if from_currency not in self.rates or to_currency not in self.rates:
            print(f"Invalid currency: {from_currency} or {to_currency}.")
            return None
        
        # Convert to base currency first, then to the target currency
        base_amount = amount / self.rates[from_currency]
        converted_amount = base_amount * self.rates[to_currency]
        return round(converted_amount, 2)

def main():
    # Replace 'your_api_key' with your actual API key
    api_key = "your_api_key"  
    converter = CurrencyConverter(api_key)
    
    base_currency = input("Enter the base currency (e.g., USD, EUR): ").upper()
    converter.fetch_exchange_rates(base_currency)
    
    while True:
        print("\nCurrency Converter Menu:")
        print("1. Convert currency")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            from_currency = input("Enter the source currency: ").upper()
            to_currency = input("Enter the target currency: ").upper()
            try:
                amount = float(input(f"Enter the amount in {from_currency}: "))
                converted = converter.convert_currency(from_currency, to_currency, amount)
                if converted is not None:
                    print(f"{amount} {from_currency} is equal to {converted} {to_currency}.")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == '2':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
