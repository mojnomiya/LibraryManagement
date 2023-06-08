

# class Person:
#     def __init__(self, name, email, username, password) -> None:
#         self.name = name
#         self.email = email
#         self.username = username
#         self.password = password

#     def __repr__(self) -> str:
#         return f"{self.name}"


# class User(Person):
#     def __init__(self, name, email, username, password) -> None:
#         super().__init__(name, email, username, password)
#         self.borrowed_books = {}

#     def borrow_books(self, books):
#         for book in books:
#             if book.quantity > 0:
#                 if book in self.borrowed_books:
#                     self.borrowed_books[book] += 1
#                 else:
#                     self.borrowed_books[book] = 1
#                 book.quantity -= 1
#                 print(f"{self.name} borrowed {book.name}")
#             else:
#                 print(f"Sorry, {book.name} is currently unavailable.")

#     def return_books(self, books):
#         for book in books:
#             if book in self.borrowed_books:
#                 if self.borrowed_books[book] > 1:
#                     self.borrowed_books[book] -= 1
#                 else:
#                     del self.borrowed_books[book]
#                 book.quantity += 1
#                 print(f"{self.name} returned {book.name}")
#             else:
#                 print(f"{self.name} did not borrow {book.name}")

#     def __repr__(self) -> str:
#         return super().__repr__()


# class Admin(Person):
#     def __init__(self, name, email, username, password):
#         super().__init__(name, email, username, password)

#     def add_book(self, library, book):
#         library.add_book(book)
#         print(f"Added {book.name} to the library.")

#     def remove_book(self, library, book):
#         library.remove_book(book)
#         print(f"Removed {book.name} from the library.")