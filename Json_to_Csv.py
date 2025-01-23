import json
import csv

def json_to_csv():
    try:
        # Take input and output file names from the user
        json_file = input("Enter the path to the input JSON file: ").strip()
        csv_file = input("Enter the desired path for the output CSV file: ").strip()

        # Open and load the JSON file
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Check if the JSON data is a list of dictionaries
        if not isinstance(data, list):
            raise ValueError("JSON file does not contain a list of objects.")

        # Extract headers from the keys of the first dictionary
        headers = data[0].keys()

        # Write the CSV file
        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)

        print(f"JSON data successfully written to {csv_file}")
    except FileNotFoundError:
        print("Error: The specified JSON file was not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Ensure the file contains valid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    json_to_csv()