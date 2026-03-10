# Write a function that accepts any object and calls a method speak() (duck typing concept).
class Dog:
    def speak(self):
        print("Bark")


class Human:
    def speak(self):
        print("I can also bark!")


def make_speak(obj):
    obj.speak()


make_speak(Dog())
make_speak(Human())
