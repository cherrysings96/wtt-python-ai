# Write a program to demonstrate polymorphism using a loop and list of objects.
class Calculator:
    def __init__(self):
        self.total = 0

    def add(self, value):
        self.total += value


c = Calculator()
l = [1, 2, 3, 4]

for i in l:
    c.add(i)

print(c.total)
