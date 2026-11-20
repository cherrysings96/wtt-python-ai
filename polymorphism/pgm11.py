# Create an example where different objects respond differently to the same function.
class A:
    def speak(self):
        print("Hi")


class B:
    def speak(self):
        print("Hello")


a = A()
b = B()
a.speak()
b.speak()
