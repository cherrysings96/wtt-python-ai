class Book:
    def __init__(self, size, author, name):
        self.size = size
        self.author = author
        self.name = name


b1 = Book(21, "JKR", "Harry Potter")
print(b1.size)
print(b1.author)
print(b1.name)
