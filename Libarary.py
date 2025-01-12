class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Copies Available: {self.copies}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}

    def add_book(self, book):
        if book.title in self.books:
            self.books[book.title].copies += book.copies
        else:
            self.books[book.title] = book
        print(f"Book '{book.title}' added to the library.")

    def borrow_book(self, title):
        if title in self.books and self.books[title].copies > 0:
            self.books[title].copies -= 1
            print(f"You have borrowed '{title}'.")
        elif title in self.books:
            print(f"'{title}' is currently unavailable.")
        else:
            print(f"'{title}' is not in the library.")

    def return_book(self, title):
        if title in self.books:
            self.books[title].copies += 1
            print(f"Thank you for returning '{title}'.")
        else:
            print(f"'{title}' does not belong to this library.")

    def view_books(self):
        if not self.books:
            print("The library has no books.")
        else:
            print("\nBooks in the library:")
            for book in self.books.values():
                print(book)

    def search_book(self, title):
        if title in self.books:
            print(f"\nBook found:\n{self.books[title]}")
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