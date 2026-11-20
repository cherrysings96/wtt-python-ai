class Laptop:
    def __init__(self, ram):
        self.__ram = ram

    def get_ram(self):
        print(self.__ram)


l = Laptop(1000)
l.get_ram()
