import pandas as pd
import os

def csv_to_json():
    """
    Convert a CSV file to a JSON file with user input for file paths and additional options.
    """
    try:
        # Get user input for CSV file path
        csv_file_path = input("Enter the path to the CSV file: ").strip()

        # Check if the CSV file exists
        if not os.path.exists(csv_file_path):
            print("Error: The specified CSV file does not exist.")
            return

        # Get user input for JSON output file path
        json_file_path = input("Enter the path to save the JSON file (e.g., output.json): ").strip()

        # Ask user for JSON formatting preference
        pretty_print = input("Do you want the JSON output to be pretty-printed? (yes/no): ").strip().lower() == "yes"

        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file_path)

        # Convert the DataFrame to JSON and save to a file
        df.to_json(
            json_file_path,
            orient="records",
            lines=False,
            indent=4 if pretty_print else None
        )

        print(f"CSV file successfully converted to JSON and saved to '{json_file_path}'.")
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
    except pd.errors.ParserError:
        print("Error: There was an issue parsing the CSV file. Please check its format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    csv_to_json()