class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def info(self):
        return f"{self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, filesize):
        super().__init__(title, author)
        self.filesize = filesize

    def info(self):
        return f"{self.title} by {self.author} (EBook {self.filesize}MB)"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book.info())
