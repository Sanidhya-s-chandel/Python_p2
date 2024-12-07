import os

if __name__ == '__main__':
    print("Welcome to the speaker .......... :)")
    while True:
        x = input("Enter what you want to speak: ")

        if x == "q" or x == "Quit" or x == "quit":
            print("Thank You for using  me !!")
            break

        command = f"echo {x}"
        os.system(command)