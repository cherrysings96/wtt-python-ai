# Demonstrate duck typing using two classes with the same method name.
class Dog:
    def bark(self):
        print("Bark")


class Human:
    def bark(self):
        print("I can also bark!")


def make_bark(obj):
    obj.bark()


make_bark(Dog())
make_bark(Human())
