class Employee:
    def __init__(self, salary):
        self._salary = salary


e = Employee(1000)
print(e._salary)
e._salary = 1200
print(e._salary)
