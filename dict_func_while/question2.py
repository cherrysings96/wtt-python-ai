student={"name":["Amina"],"marks":[80,90,100]}

marks=student["marks"]
avg=sum(marks)/len(marks)

student["average"]=avg

if avg>=90:
    grade="A"
elif avg>=80:
    grade="B"
elif avg>=70:
    grade="C"
elif avg>=60:
    grade="D"
else:
    grade="F"

student["grade"]=grade

print(student)