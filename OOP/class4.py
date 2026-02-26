class House:
    def __init__(self, color, floors, rooms):
        self.color = color
        self.floors = floors
        self.rooms = rooms

    def Price(self):
        if self.floors and self.rooms >= 3:
            return "The house is expensive"
        else:
            return "The house is affordable"

    def Show_details(self):
        return f"The house is {self.color}, has {self.floors} floors,and {self.rooms} rooms."


h1 = House("pink", 3, 2)
print(h1.Price())
print(h1.Show_details())
