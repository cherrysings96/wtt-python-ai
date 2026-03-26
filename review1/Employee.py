class Employee:
    def __init__(self, name, classname):
        self.name = name
        self.classname = classname
    def display(self):
        print(f"Name: {self.name}, Class: {self.classname}")    
emp1 = Employee("John Doe", "A")
emp1.display()  

        
