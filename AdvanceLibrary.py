import json

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "copies": self.copies
        }

    @staticmethod
    def from_dict(data):
        return Book(data['title'], data['author'], data['copies'])


class Library:
    def __init__(self, name, data_file="library_data.json"):
        self.name = name
        self.data_file = data_file
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.data_file, "r") as file:
                data = json.load(file)
                return {title: Book.from_dict(book) for title, book in data.items()}
        except FileNotFoundError:
            return {}

    def save_books(self):
        with open(self.data_file, "w") as file:
            json.dump({title: book.to_dict() for title, book in self.books.items()}, file, indent=4)

    def add_book(self, book):
        if book.title in self.books:
            self.books[book.title].copies += book.copies
        else:
            self.books[book.title] = book
        self.save_books()
        print(f"Book '{book.title}' added to the library.")

    def borrow_book(self, title):
        if title in self.books and self.books[title].copies > 0:
            self.books[title].copies -= 1
            self.save_books()
            print(f"You have borrowed '{title}'.")
        elif title in self.books:
            print(f"'{title}' is currently unavailable.")
        else:
            print(f"'{title}' is not in the library.")

    def return_book(self, title):
        if title in self.books:
            self.books[title].copies += 1
            self.save_books()
            print(f"Thank you for returning '{title}'.")
        else:
            print(f"'{title}' does not belong to this library.")

    def view_books(self):
        if not self.books:
            print("The library has no books.")
        else:
            print("\nBooks in the library:")
            for book in self.books.values():
                print(f"Title: {book.title}, Author: {book.author}, Copies Available: {book.copies}")

    def search_book(self, title):
        if title in self.books:
            book = self.books[title]
            print(f"\nBook found: Title: {book.title}, Author: {book.author}, Copies Available: {book.copies}")
        else:
            print(f"'{title}' is not available in the library.")


# Main Program
if __name__ == "__main__":
    library = Library("City Library")

    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            copies = int(input("Enter number of copies: "))
            book = Book(title, author, copies)
            library.add_book(book)
        elif choice == "2":
            title = input("Enter the book title to borrow: ")
            library.borrow_book(title)
        elif choice == "3":
            title = input("Enter the book title to return: ")
            library.return_book(title)
        elif choice == "4":
            library.view_books()
        elif choice == "5":
            title = input("Enter the book title to search: ")
            library.search_book(title)
        elif choice == "6":
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")