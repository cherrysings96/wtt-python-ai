# Create a parent class Shape and two child classes Circle and Rectangle with different implementations of area calculation.
class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


circle = Circle(5)
rectangle = Rectangle(4, 6)
print("Circle area:", circle.area())
print("Rectangle area:", rectangle.area())
