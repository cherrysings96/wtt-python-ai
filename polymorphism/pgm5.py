# Create a class that overloads the + operator using __add__().
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages+other.pages


print(Book(10)+Book(500))
