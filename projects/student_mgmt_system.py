from abc import ABC, abstractmethod


class AbstractSystem(ABC):
    @abstractmethod
    def generate_report(self):
        pass


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name:-{self.name}\nAge:-{self.age}")


class Student(Person, AbstractSystem):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course
        self.__marks = 0

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks! Must be between 0-100. ")

    def get_marks(self):
        return self.__marks

    def display(self):
        print("Student Management System")
        print("-"*25)
        super().display()
        print(f"ID:-{self.student_id}")
        print(f"Course:-{self.course}")
        print(f"Marks:-{self.__marks}")
        print("I am a student.")

    def generate_report(self):
        print("Student report generated!\n\n")


student1 = Student("Sherene", 29, "LBT15IT039", "IT")
student2 = Student("Rakhi", 26, "UIT14038", "EC")

student1.set_marks(80)
student1.display()
student1.generate_report()

student2.set_marks(90)
student2.display()
student2.generate_report()
