class Bookshelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books"


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"

    def count(self, x, y):
        return x + y



book = Book("Harry Potter")
book2 = Book("Python 101")
shelf = Bookshelf(book, book2)

print(type(shelf))
print(shelf)