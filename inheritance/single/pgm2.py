class Animal:
    def show(self):
        print("Animal")


class Dog(Animal):
    def show2(self):
        print("Dog")


d = Dog()
d.show()
d.show2()
