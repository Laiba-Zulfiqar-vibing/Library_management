# -----------------------------
# Book class definition
# -----------------------------
class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity

    def display_book_info(self):
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Quantity: {self.quantity}")

    def check_availability(self):
        return self.quantity > 0

    def update_quantity(self, change):
        self.quantity += change


# -----------------------------
# User class definition
# -----------------------------
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.check_availability():
            self.borrowed_books.append(book)
            book.update_quantity(-1)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.update_quantity(1)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")


# -----------------------------
# Library class definition
# -----------------------------
class Library:
    def __init__(self):
        self.books = [
            Book(1, "undying affinity", "sara naveed", 5),
            Book(2, "jannat ky paty", "nimra ahmed", 3),
            Book(3, "namal", "nimra ahmed", 4),
            Book(4, "peere kamil", "umaira ahmed", 2)
        ]
        self.users = [User(1, "Alice")]

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully!")

    def list_books(self):
        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                book.display_book_info()

    def search_book_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def register_user(self, user):
        if any(u.user_id == user.user_id for u in self.users):
            print("User ID already exists!")
        else:
            self.users.append(user)
            print(f"User {user.name} registered successfully!")

    def borrow_book(self, user_id, book_id):
        user = next((u for u in self.users if u.user_id == user_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)
        if user and book:
            user.borrow_book(book)
        else:
            print("Invalid User ID or Book ID.")

    def return_book(self, user_id, book_id):
        user = next((u for u in self.users if u.user_id == user_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)
        if user and book:
            user.return_book(book)
        else:
            print("Invalid User ID or Book ID.")


# -----------------------------
# Main Program
# -----------------------------
def main():
    library = Library()

    while True:
        print("\n===== Library Management System =====")
        print("1. View All Books")
        print("2. Add Book")
        print("3. Search Book by Title")
        print("4. Register User")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            library.list_books()

        elif choice == '2':
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            quantity = int(input("Enter Quantity: "))
            library.add_book(Book(book_id, title, author, quantity))

        elif choice == '3':
            title = input("Enter Title to Search: ")
            results = library.search_book_by_title(title)
            if results:
                for book in results:
                    book.display_book_info()
            else:
                print("No matching books found.")

        elif choice == '4':
            user_id = int(input("Enter User ID: "))
            name = input("Enter User Name: ")
            library.register_user(User(user_id, name))

        elif choice == '5':
            user_id = int(input("Enter User ID: "))
            book_id = int(input("Enter Book ID to Borrow: "))
            library.borrow_book(user_id, book_id)

        elif choice == '6':
            user_id = int(input("Enter User ID: "))
            book_id = int(input("Enter Book ID to Return: "))
            library.return_book(user_id, book_id)

        elif choice == '7':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")



main()