class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.is_checked_out = False

    def checkout(self):
        if self.is_checked_out:
            print(f'{self.title} is already checked out.')
        else:
            self.is_checked_out = True
            print(f'{self.title} has been checked out.')

    def checkin(self):
        if not self.is_checked_out:
            print(f'{self.title} is already not checked out.')
        else:
            self.is_checked_out = False
            print(f'{self.title} has been checked in.')


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'{book.title} has been added to the library.')

    def checkout_book(self, ISBN):
        for book in self.books:
            if book.ISBN == ISBN:
                book.checkout()
                return
        print(f'Book with ISBN {ISBN} not found.')

    def checkin_book(self, ISBN):
        for book in self.books:
            if book.ISBN == ISBN:
                book.checkin()
                return
        print(f'Book with ISBN {ISBN} not found.')


alex = Library('The library of alex')

book1 = Book("The Alchemist","Paulo Coelho", 9780062315007)
book2 = Book("To Kill a Mockingbird","Harper Lee", 9780099466734)

alex.add_book(book1)
alex.add_book(book2)

alex.checkout_book(9780099466734)

print(alex.name)