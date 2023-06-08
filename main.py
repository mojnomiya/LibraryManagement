from library import Library, User, Admin
from book import Book

def main():
    book1 = Book('Gulliver\'s Travels', 'Jonathan Swift', 5, 'First')
    book2 = Book('Sherlock Holmes', 'Arthur Conan Doyle', 10)

    phitron = Library()
    phitron.add_book(book1)
    phitron.add_book(book2)

    # phitron.remove_book(book1)
    

    abul = User('Abul', 'abul@gmail.com', 'abul', 'abul')
    babul = User('Babul', 'babul@gmail.com', 'babul', 'babul')
    mokbul = User('Mokbul', 'mokbul@gmail.com', 'mokbul', 'mokbul')

    phitron.add_user(abul)
    phitron.add_user(babul)
    phitron.add_user(mokbul)
    # phitron.show_users()

    admin = Admin('Admin', 'admin@admin.com', 'admin', 'password')
    phitron.add_admin(admin)

    choice = landing(phitron)
    if choice == '1':
        login_stat = phitron.log_in('user', phitron)
        # if login_stat:
            # user_choice = user_dashboard()
    elif choice == '2':
        phitron.user_sign_up(phitron)
    elif choice == '3':
        phitron.log_in('admin', phitron)
    elif choice == '4':
        phitron.admin_sign_up(phitron)

def landing(phitron):
    print("====================Phitron Library=====================\n")
    phitron.available_books()
    print()
    print("1. User Log in")
    print("2. User Sign up")
    print("3. Admin Log in")
    print("4. Admin Sign up")
    choice = input('Enter your choice: ')
    return choice




if __name__ == '__main__':
    main()