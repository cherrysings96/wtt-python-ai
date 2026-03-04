class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color


c = Car("Toyota", "pink")
print(c.brand)
# print(c.color)
c.color = "red"
print(c.color)
