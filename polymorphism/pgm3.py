# Write a program showing runtime polymorphism using a Vehicle class.
class Vehicle:
    def run(self):
        print("Vehicle is running")


class Car(Vehicle):
    def run(self):
        print("Car is running safely on 4 wheels")


class Bike(Vehicle):
    def run(self):
        print("Bike is zooming on 2 wheels")


# Instead of calling them individually, let's treat them as a collection
garage = [Vehicle(), Car(), Bike()]

# The "Runtime Polymorphism" happens here:
for vehicle in garage:
    vehicle.run()
