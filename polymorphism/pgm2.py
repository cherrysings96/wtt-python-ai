class Shape:
    def area(self):
        return "Shape method executed"


class Circle(Shape):

    def area(self):
        return "Circle method executed"


class Rectangle(Shape):

    def area(self):
        return "Rectangle method executed"


c = Circle()
r = Rectangle()
print(c.area())
print(r.area())
