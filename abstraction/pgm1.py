from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def area(self, r):
        return 3.14*r*r


class Rectangle(Shape):
    def area(self, l, w):
        return l*w


c = Circle()
r = Rectangle()

print(c.area(3))
print(r.area(12, 3))
