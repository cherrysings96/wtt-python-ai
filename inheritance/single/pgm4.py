class Shape:
    def __init__(self, color):
        self.color = color

    def show_color(self):
        print(self.color)


class Circle(Shape):
    def __init__(self, color, circum):
        super().__init__(color)
        self.circum = circum

    def show_circum(self):
        super().show_color()
        print(self.circum)


c = Circle("blue", 100)
c.show_circum()
