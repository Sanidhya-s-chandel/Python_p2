import emoji
import json

def emoji_to_text(input_string):
    """
    Converts emojis in the input string to their textual descriptions.

    :param input_string: The string containing emojis.
    :return: A string with emojis replaced by their textual descriptions.
    """
    return emoji.demojize(input_string)

def batch_convert_emoji(file_path):
    """
    Reads a file with text containing emojis, converts them to text, and saves the output.

    :param file_path: Path to the input file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        converted_content = emoji_to_text(content)

        output_file = file_path.replace('.txt', '_converted.txt')
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(converted_content)

        print(f"Converted content saved to {output_file}")
    except FileNotFoundError:
        print("Error: File not found. Please provide a valid file path.")

def display_menu():
    """
    Displays the main menu for the emoji converter.
    """
    print("\nEmoji to Text Converter")
    print("1. Convert a single text string")
    print("2. Convert emojis in a file (batch processing)")
    print("3. Exit")

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            text = input("Enter a string with emojis: ")
            result = emoji_to_text(text)
            print("Converted Text:", result)
        elif choice == '2':
            file_path = input("Enter the file path for batch conversion: ")
            batch_convert_emoji(file_path)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")