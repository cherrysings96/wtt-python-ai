# Show how *args can be used to simulate method overloading.

class Show_num:
    def show(self, *args):
        print("Value:", args)


c = Show_num()
c.show(1, 2)
c.show(2, 3, 4)
c.show(5, 5)
