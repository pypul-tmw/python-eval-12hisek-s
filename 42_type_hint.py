class Book:
    def __init__(self, title:str, isbn:str):
        self.title = title
        self.isbn = isbn

    def get_title(self) -> str:
        return self.title


book = Book("The Alchemist", "12345")
print(book.get_title())