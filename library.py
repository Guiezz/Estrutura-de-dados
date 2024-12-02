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
                return_date = input("Enter return date: ")
                current.return_date = return_date
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
                    current.id, current.next.id = current.next.id, current.id
                    current.name, current.next.name = current.next.name, current.name
                    changed = True
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
                    print("3: Return to Main Menu")
                    sub_option = int(input("Choose an option: "))
                    
                    if sub_option == 1:
                        library.collection.show_collection()
                    elif sub_option == 2:
                        book_id = int(input("Enter book ID to borrow: "))
                        library.collection.borrow_book(book_id, 14)  # Example: return in 14 days
                    elif sub_option == 3:
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
