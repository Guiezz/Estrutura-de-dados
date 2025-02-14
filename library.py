"""
Implementação e Gerenciamento de um Acervo de Livros Utilizando Lista
Simplesmente Encadeada em Python.
Fácil
  Descrição: Desenvolva um programa em Python para gerenciar o acervo de uma
  biblioteca utilizando uma lista simplesmente encadeada. O programa deve conter
  as seguintes funcionalidades:
  1:  Inserir o livro (inserir após um ID específico)
  2:  Deletar um livro da lista
  3:   Exibir a lista
  4:   A Classe livro deve ter nome, ID e data de devolução
Médio
  Faça uma lista para o preenchimento de usuários. O usuário pode pedir
  emprestado até 3 livros em paralelo.
"""

class Book:
    def __init__(self, id, name, return_date):
        self.id = id
        self.name = name
        self.return_date = return_date
        self.next = None  
        self.is_borrowed = False  

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"ID: {self.id}, Name: {self.name}, Return Date: {self.return_date}, Status: {status}"


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.borrowed_books = [] 

    def __str__(self):
        borrowed_books = ', '.join([book.name for book in self.borrowed_books]) or "No books borrowed"
        return f"User ID: {self.id}, Name: {self.name}, Borrowed Books: [{borrowed_books}]"


class Library:
    def __init__(self):
        self.head = None 
        self.users = {}  
        self.init_library()

    def init_library(self):
        initial_books = [
            Book(1, "Book 1", "01/01/2022"),
            Book(2, "Book 2", "01/01/2022"),
            Book(3, "Book 3", "01/01/2022"),
            Book(4, "Book 4", "01/01/2022"),
            Book(5, "Book 5", "01/01/2022")
        ]

        previous_book = None
        for book in initial_books:
            if self.head is None:
                self.head = book
            else:
                previous_book.next = book
            previous_book = book

    def add_new_user(self, id, name):
        if id in self.users:
            print("User ID already exists!")
            return
        self.users[id] = User(id, name)
        print(f"User {name} added successfully!")

    def borrow_book(self, user_id, book_id):
        if user_id not in self.users:
            print("User not found!")
            return

        user = self.users[user_id]
        if len(user.borrowed_books) >= 3:
            print(f"User {user.name} has already borrowed 3 books!")
            return

        current = self.head
        while current:
            if current.id == book_id:
                if current.is_borrowed:
                    print(f"Book '{current.name}' is already borrowed!")
                    return

                current.is_borrowed = True
                user.borrowed_books.append(current)
                print(f"Book '{current.name}' borrowed by {user.name}!")
                return
            current = current.next

        print("Book not found!")

    def return_book(self, user_id, book_id):
        if user_id not in self.users:
            print("User not found!")
            return

        user = self.users[user_id]
        for book in user.borrowed_books:
            if book.id == book_id:
                book.is_borrowed = False
                user.borrowed_books.remove(book)
                print(f"Book '{book.name}' returned to the library!")
                return

        print("Book not found in user's borrowed books!")

    def show_library(self):
        print("Library Books:")
        current = self.head
        while current:
            print(current)
            current = current.next

    def show_users(self):
        print("Users:")
        for user in self.users.values():
            print(user)


def main():
    library = Library()

    while True:
        print("\nOptions:")
        print("1: Add new user")
        print("2: Borrow book")
        print("3: Return book")
        print("4: Show library")
        print("5: Show users")
        print("6: Exit")
        option = int(input("Choose an option: "))

        if option == 1:
            user_id = int(input("Enter user ID: "))
            name = input("Enter user name: ")
            library.add_new_user(user_id, name)

        elif option == 2:
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))
            library.borrow_book(user_id, book_id)

        elif option == 3:
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID to return: "))
            library.return_book(user_id, book_id)

        elif option == 4:
            library.show_library()

        elif option == 5:
            library.show_users()

        elif option == 6:
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()





=======
from datetime import datetime, timedelta


class Book:
    def __init__(self, id, name, return_date=None):
        self.id = id
        self.name = name
        self.return_date = return_date
        self.next = None
        self.previous = None  
        self.is_borrowed = False  

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"ID: {self.id}, Name: {self.name}, Return Date: {self.return_date}, Status: {status}"

class Collection:
    def __init__(self):
        self.head = None
        self.tail = None
        self.init_collection()

    def init_collection(self):
        initial_books = [
            (1, "Romance"),
            (2, "Fantasia"),
            (3, "Misterio"),
            (4, "Terror"),
            (5, "Aventura"),
            (6, "Culinária")
        ]
        previous_book = None
        for id, name in initial_books:
            new_book = Book(id, name)
            if self.head is None:
                self.head = new_book
            else:
                previous_book.next = new_book
                new_book.previous = previous_book
            previous_book = new_book
        self.tail = previous_book

    def add_new_book(self, id, name):
        new_book = Book(id, name)
        if not self.head:
            self.head = new_book
            return
        self.tail.next = new_book
        new_book.previous = self.tail
        self.tail = new_book

    def remove_book(self, id):
        current = self.head
        while current and current.id != id:
            current = current.next
        if current is None:
            print("Book not found")
            return
        if current.previous:
            current.previous.next = current.next
        if current.next:
            current.next.previous = current.previous
        if current == self.head:
            self.head = current.next
        if current == self.tail:
            self.tail = current.previous
        print(f"Book {id} removed")

    def first_book(self):
        return self.head

    def show_collection(self):
        current = self.head
        while current:
            print(current)
            current = current.next

    def search_book(self, id):
        current = self.head
        while current:
            if current.id == id:
                print("Book found!")
                print(current)
                return
            current = current.next
        print("Book not found")

    def borrow_book(self, id, return_days):
        current = self.head
        while current:
            if current.id == id:
                return_date = datetime.now() + timedelta(days=return_days)
                current.return_date = return_date.strftime("%d/%m/%Y")
                current.is_borrowed = True
                print(f"Book {id} borrowed, return date: {return_date}")
                return
            current = current.next
        print("Book not found")

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.next = None
        self.previous = None
    
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

class Library:
    def __init__(self):
        self.users_head = None
        self.users_tail = None
        self.collection = Collection()
        self.init_users()

    def init_users(self):
        initial_users = [
            (1, "Maria"),
            (2, "Guilherme"),
            (3, "David"),
        ]

        previous_user = None
        for id, name in initial_users:
            new_user = User(id, name)
            if self.users_head is None:
                self.users_head = new_user
            else:
                previous_user.next = new_user
                new_user.previous = previous_user
            previous_user = new_user
        self.users_tail = previous_user

    def add_user(self, id, name):
        new_user = User(id, name)
        if not self.users_head:
            self.users_head = new_user
            self.users_tail = new_user
            return
        self.users_tail.next = new_user
        new_user.previous = self.users_tail
        self.users_tail = new_user

    def remove_user(self, id):
        current = self.users_head
        while current and current.id != id:
            current = current.next
        if current is None:
            print("User not found")
            return
        if current.previous:
            current.previous.next = current.next
        if current.next:
            current.next.previous = current.previous
        if current == self.users_head:
            self.users_head = current.next
        if current == self.users_tail:
            self.users_tail = current.previous
        print(f"User with ID {id} removed")

    def list_users(self):
        current = self.users_head
        while current:
            print(current)
            current = current.next

    def search_user_by_id(self, id):
        current = self.users_head
        while current:
            if current.id == id:
                return current
            current = current.next
        return None
    
    def sort_list_by_id(self):
        if self.users_head is None or self.users_head.next is None:
            return

        changed = True
        while changed:
            changed = False
            current = self.users_head
            while current and current.next:
                if current.id > current.next.id:
                    if current.previous:
                        current.previous.next = current.next
                    if current.next.next:
                        current.next.next.previous = current
                    
                    temp = current.next
                    current.next = temp.next
                    temp.next = current
                    temp.previous = current.previous
                    current.previous = temp

                    if temp.previous is None:
                        self.users_head = temp
                    if current.next is None:
                        self.users_tail = current

                    changed = True
                else:
                    current = current.next





def main():
    library = Library()

    while True:
        print("\nOptions:")
        print("1: List Users")
        print("2: Add User")
        print("3: Remove User")
        print("4: Show Library Collection")
        print("5: Select User and Manage Collection")
        print("6: Sort list")
        print("7: Exit")
        option = int(input("Choose an option: "))

        if option == 1:
            library.list_users()

        elif option == 2:
            user_id = int(input("Enter user ID: "))
            user_name = input("Enter user name: ")
            library.add_user(user_id, user_name)
            print("User added successfully")

        elif option == 3:
            user_id = int(input("Enter user ID to remove: "))
            library.remove_user(user_id)

        elif option == 4:
            library.collection.show_collection()

        elif option == 5:
            user_id = int(input("Enter user ID: "))
            user = library.search_user_by_id(user_id)
            if user:
                print(f"Managing collection for {user.name}")
                while True:
                    print("\nOptions for managing books:")
                    print("1: Show Collection")
                    print("2: Borrow Book")
                    print("3: Add new book")
                    print("4: Remove book")
                    print("5: Search book by ID")
                    print("6: Return to Main Menu")
                    sub_option = int(input("Choose an option: "))
                    
                    if sub_option == 1:
                        library.collection.show_collection()
                    elif sub_option == 2:
                        book_id = int(input("Enter book ID to borrow: "))
                        return_days = int(input("Enter number of days to return book: "))
                        library.collection.borrow_book(book_id, return_days)
                    elif sub_option == 3:
                        book_id = int(input("Enter book ID to add: "))
                        book_name = input("Enter book name to add: ")
                        library.collection.add_new_book(book_id, book_name)
                        print("Book added successfully")
                    elif sub_option == 4:
                        book_id = int(input("Enter book ID to remove: "))
                        library.collection.remove_book(book_id)
                    elif sub_option == 5:
                        book_id = int(input("Enter book ID to search: "))
                        library.collection.search_book(book_id)
                    elif sub_option == 6:
                        break
                    else:
                        print("Invalid option! Please try again.")
            else:
                print("User not found!")
        
        elif option == 6:
            library.sort_list_by_id()

        elif option == 7:
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()
