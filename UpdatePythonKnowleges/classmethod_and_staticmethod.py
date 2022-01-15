# example 1 ______________________________________

class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print(f"Called static_method.")


# example 2 ______________________________________

class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    def setCoords(self, x, y):  # method has access to all methods(@classmethod, @staticmethod) and class attributes
        if Vector.validate(x) and Vector.validate(y):  # by the 'self' object has access to instance of class
            self.x = x
            self.y = y

    @classmethod
    def validate(cls, arg):
        if cls.MIN_COORD <= arg <= cls.MAX_COORD:
            return True
        return False

    @staticmethod  # has not access:attributes,to usual methods or @classmethod, or instance of class: v = Vector (2, 1)
    def norm2(x, y):
        return x * x + y * y


v = Vector()
print(v)
v.setCoords(1, 2)


# example 3 ______________________________________


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, {self.weight} gr.>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, Book.TYPES[1], page_weight)  # we may write 'cls' instead of 'Book'


book = Book("Harry Potter", "comic book", 1500)  # we access to class through the method, object created by method
light_book = Book.paperback("Python PEP", 600)

print(book)
print(light_book)


# example 4 HOME_TASK ______________________________________

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({'name': name, 'price': price})

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return int(total)

    @classmethod
    def franchise(cls, store):
        return cls(store.name + ' - franchise')
        # Return another store, with the same name as the argument's name, plus " - franchise"

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        return f'{store.name}, total stock price: {store.stock_price()}'
        # It should be in the format 'NAME, total stock price: TOTAL'


store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)

Store.franchise(store)
Store.franchise(store2)

Store.store_details(store)
Store.store_details(store2)
