class Student:
    def __init__(self, marks):
        self.__marks = marks

    def set_marks(self):
        while self.__marks > 0 and self.__marks < 100:
            print(self.__marks)
            break
        else:
            print("Invalid")


s = Student(100)
s.set_marks()
