class Grandparent:

    def __init__(self, trait1):
        self.trait1 = trait1

    def show_grand(self):
        print(self.trait1)


class Parent(Grandparent):

    def __init__(self, trait1, trait2):
        super().__init__(trait1)
        self.trait2 = trait2

    def show_parent(self):
        print(self.trait2)


class Child(Parent):

    def __init__(self, trait1, trait2, trait3):
        super().__init__(trait1, trait2)
        self.trait3 = trait3

    def show_child(self):
        print(self.trait3)


c = Child("Knit", "Work", "Play")
c.show_grand()
c.show_parent()
c.show_child()
