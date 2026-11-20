class Animal():
    def Sound(self):
        print("Animal method executed.")


class Dog(Animal):
    def Sound(self):
        print("Dog method executed.")
        print("\nOverriding successful!")


d = Dog()
d.Sound()
