class Person:
    def show(self):
        print("Person")


class Student(Person):
    def show2(self):
        print("Student")


s = Student()
s.show()
s.show2()
