import os

class FileManager:
    def __init__(self, base_path="."):
        """
        Initialize the FileManager with a base path.
        """
        self.base_path = os.path.abspath(base_path)
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)
        print(f"File Manager initialized at: {self.base_path}")

    def create_file(self, file_name, content=""):
        """
        Create a new file with the specified content.
        """
        file_path = os.path.join(self.base_path, file_name)
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"File '{file_name}' created successfully at {self.base_path}.")

    def read_file(self, file_name):
        """
        Read and display the content of a file.
        """
        file_path = os.path.join(self.base_path, file_name)
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                content = file.read()
            print(f"Content of '{file_name}':\n{content}")
        else:
            print(f"File '{file_name}' does not exist.")

    def update_file(self, file_name, content):
        """
        Update an existing file by appending content.
        """
        file_path = os.path.join(self.base_path, file_name)
        if os.path.exists(file_path):
            with open(file_path, 'a') as file:
                file.write(content)
            print(f"File '{file_name}' updated successfully.")
        else:
            print(f"File '{file_name}' does not exist.")

    def delete_file(self, file_name):
        """
        Delete a specified file.
        """
        file_path = os.path.join(self.base_path, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File '{file_name}' deleted successfully.")
        else:
            print(f"File '{file_name}' does not exist.")

    def create_folder(self, folder_name):
        """
        Create a new folder.
        """
        folder_path = os.path.join(self.base_path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Folder '{folder_name}' created successfully.")
        else:
            print(f"Folder '{folder_name}' already exists.")

    def list_files_and_folders(self):
        """
        List all files and folders in the base path.
        """
        print(f"Contents of '{self.base_path}':")
        for item in os.listdir(self.base_path):
            item_path = os.path.join(self.base_path, item)
            if os.path.isdir(item_path):
                print(f"📁 {item}")
            else:
                print(f"📄 {item}")

    def delete_folder(self, folder_name):
        """
        Delete a specified folder and its contents.
        """
        folder_path = os.path.join(self.base_path, folder_name)
        if os.path.exists(folder_path):
            try:
                os.rmdir(folder_path)
                print(f"Folder '{folder_name}' deleted successfully.")
            except OSError:
                print(f"Folder '{folder_name}' is not empty. Remove its contents first.")
        else:
            print(f"Folder '{folder_name}' does not exist.")


# Main program to interact with the FileManager
def main():
    manager = FileManager()

    while True:
        print("\nFile Management System")
        print("1. Create File")
        print("2. Read File")
        print("3. Update File")
        print("4. Delete File")
        print("5. Create Folder")
        print("6. List Files and Folders")
        print("7. Delete Folder")
        print("8. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            file_name = input("Enter file name: ")
            content = input("Enter content (leave blank for an empty file): ")
            manager.create_file(file_name, content)

        elif choice == '2':
            file_name = input("Enter file name: ")
            manager.read_file(file_name)

        elif choice == '3':
            file_name = input("Enter file name: ")
            content = input("Enter content to append: ")
            manager.update_file(file_name, content)

        elif choice == '4':
            file_name = input("Enter file name: ")
            manager.delete_file(file_name)

        elif choice == '5':
            folder_name = input("Enter folder name: ")
            manager.create_folder(folder_name)

        elif choice == '6':
            manager.list_files_and_folders()

        elif choice == '7':
            folder_name = input("Enter folder name: ")
            manager.delete_folder(folder_name)

        elif choice == '8':
            print("Exiting File Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()