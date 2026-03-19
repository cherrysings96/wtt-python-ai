class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def ShowAll(self):
        print(f"Name={self.name}")
        print(f"Salary={self.salary}")


e = Employee("Sherene", 20000)
e.ShowAll()
