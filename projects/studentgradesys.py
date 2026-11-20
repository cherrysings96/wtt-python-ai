l = ["Sherene", "Rakhi", "Amina"]
marks = []
for name in l:
    print("Student Name:", name)
    marks.append(int(input("Enter your marks: ")))


def checkgrade(l, marks):
    for i in range(len(l)):
        name = l[i]
        mark = marks[i]
        if mark >= 90:
            grade = "A"
        elif mark >= 80:
            grade = "B"
        elif mark >= 70:
            grade = "C"
        elif mark >= 60:
            grade = "D"
        else:
            grade = "F"
        output(name, mark, grade)


def output(name, mark, grade):
    print(name, "has received", mark,
          "for Python and has gotten a final grade of:", grade)


checkgrade(l, marks)
