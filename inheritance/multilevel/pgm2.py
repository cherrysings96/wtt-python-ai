class Mammal:

    def __init__(self, legs):
        self.legs = legs

    def show_legs(self):
        print("2 legs or 4")


class Dog(Mammal):

    def __init__(self, legs, tail):
        super().__init__(legs)
        self.tail = tail

    def show_tail(self):
        print("Has")


class Puppy(Dog):
    def __init__(self, legs, tail, age):
        super().__init__(legs, tail)
        self.age = age

    def show_age(self):
        print("Below 2")


p = Puppy(2, "yes", 1)
p.show_legs()
p.show_tail()
p.show_age()

print(p.legs, p.tail, p.age)
