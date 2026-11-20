# class Vehicle:
#     def __init__(self, wheels):
#         self.wheels = wheels
#         print("Vehicle constructor executed")

#     def show(self):
#         print(f"No. of wheels:{self.wheels}.")


# class Car(Vehicle):
#     def __init__(self, wheels, types):
#         super().__init__(wheels)
#         self.types = types
#         print("Car constructor executed")

#     def show2(self):
#         print(f"Type:{self.types}.")


# c = Car(10, "Mitsubitshi")
# c.show()
# c.show2()

class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels
        print("Vehicle constructor executed")

    def get_wheels(self):
        return self.wheels


class Car(Vehicle):
    def __init__(self, wheels, brand):
        super().__init__(wheels)
        self.brand = brand
        print("Car constructor executed")

    def get_brand(self):
        return self.brand


c = Car(4, "BMW")
print(f"Wheels:{c.get_wheels()}")
print(f"Brand:{c.get_brand()}")
