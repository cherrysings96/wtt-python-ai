# Create a parent class Vehicle and two child classes Car and Bike.
# Add a common method in the parent class and call it from both child classes.

class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

    def show_wheels(self):
        return self.wheels


class Car(Vehicle):

    def __init__(self, wheels, cwheel):
        super().__init__(wheels)
        self.cwheel = cwheel

    def show_cwheel(self):
        return self.cwheel


class Bike(Vehicle):

    def __init__(self, wheels, bwheel):
        super().__init__(wheels)
        self.bwheel = bwheel

    def show_bwheel(self):
        return self.bwheel


b = Bike("2 or 4", 2)
c = Car("2 or 4", 4)

print(
    f"A vehicle has {b.show_wheels()} wheels and a bike has {b.show_bwheel()} wheels.")

print(
    f"A vehicle has {c.show_wheels()} wheels and a car has {c.show_cwheel()} wheels.")
