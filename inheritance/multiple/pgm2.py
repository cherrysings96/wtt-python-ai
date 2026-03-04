class Teacher:
    def teach(self):
        print("Teach")


class Researcher:
    def research(self):
        print("Research")


class Professor(Teacher, Researcher):
    def lab(self):
        print("I have lab work")


p = Professor()
p.teach()
p.research()
p.lab()
