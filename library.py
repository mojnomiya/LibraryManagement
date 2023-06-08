import sys

class Library:
    def __init__(self):
        self.books = []
        self.users = {}
        self.admins = {}

    def add_user(self, user):
        self.users[user.username] = user

    def show_users(self):
        for user in self.users.values():
            print(user)

    def add_admin(self, admin):
        self.admins[admin.username] = admin

    def available_books(self):
        print("--------------------Available Books---------------------")
        for book in self.books:
            print(book)

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.name} to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Removed {book.name} from the library.")

    @staticmethod
    def log_in(person, library):
        if person == "user":
            Library.user_login(library)
        else:
            Library.admin_login(library)

    @staticmethod
    def user_login(library):
        username = input("Enter username or email: ")
        password = input("Enter password: ")
        user = library.users.get(username)
        if user and user.password == password:
            print("Successfully logged in\n")
            UserActions.user_dashboard(user)
            # Continue with user actions
        else:
            print("Incorrect username or password")

    @staticmethod
    def admin_login(library):
        username = input("Enter username or email: ")
        password = input("Enter password: ")
        admin = library.admins.get(username)
        if admin and admin.password == password:
            print("Successfully logged in\n")
            # Continue with admin actions
        else:
            print("Incorrect username or password")

    @staticmethod
    def user_sign_up(library):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        user = User(name, email, username, password)
        library.add_user(user)
        print("User account created successfully!\n")

    @staticmethod
    def admin_sign_up(library):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        admin = Admin(name, email, username, password)
        library.add_admin(admin)
        print("Admin account created successfully!\n")


class Person:
    def __init__(self, name, email, username, password) -> None:
        self.name = name
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self) -> str:
        return f"{self.name}"


class User(Person):
    def __init__(self, name, email, username, password) -> None:
        super().__init__(name, email, username, password)
        

    def __repr__(self) -> str:
        return super().__repr__()


class UserActions(User):
    def __init__(self, name, email, username, password) -> None:
        super().__init__(name, email, username, password)
        self.borrowed_books = {}

    def borrow_books(self, books):
        for book in books:
            if book.quantity > 0:
                if book in self.borrowed_books:
                    self.borrowed_books[book] += 1
                else:
                    self.borrowed_books[book] = 1
                book.quantity -= 1
                print(f"{self.name} borrowed {book.name}")
            else:
                print(f"Sorry, {book.name} is currently unavailable.")

    def return_books(self, books):
        for book in books:
            if book in self.borrowed_books:
                if self.borrowed_books[book] > 1:
                    self.borrowed_books[book] -= 1
                else:
                    del self.borrowed_books[book]
                book.quantity += 1
                print(f"{self.name} returned {book.name}")
            else:
                print(f"{self.name} did not borrow {book.name}")

    
    def user_dashboard(self):
        print(f'Hello {self.name}, Welcome to your dashboard\n')
        print('1. Show Borrowed Books')
        print('2. Borrow Book')
        print('3. Return Book')
        print('4. Log out')
        print('5. Exit')
        user_choice = input("Enter your choice: ")
        if user_choice == '1':
                ...
        elif user_choice == '2':
            self.borrow_books()
        elif user_choice == '3':
            book_code = input("Enter book code: ")
            # self.return_books()
        elif user_choice == '4':
            pass
        elif user_choice == '5':
            sys.exit("Succesfully Exited")

class Admin(Person, Library):
    def __init__(self, name, email, username, password):
        super().__init__(name, email, username, password)

    def add_book(self, book):
        return super().add_book(book)

    def remove_book(self, book):
        return super().remove_book(book)



