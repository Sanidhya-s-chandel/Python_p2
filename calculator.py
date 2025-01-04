def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

def calculator():
    print("Welcome to the Python Calculator!")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    while True:
        try:
            choice = input("\nEnter the operation (1/2/3/4/5): ")
            
            if choice == '5':
                print("Exiting the calculator. Goodbye!")
                break

            if choice in ['1', '2', '3', '4']:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == '1':
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
            else:
                print("Invalid input. Please select a valid operation.")

        except ValueError:
            print("Error: Invalid input. Please enter numbers only.")

# Run the calculator
calculator()