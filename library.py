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