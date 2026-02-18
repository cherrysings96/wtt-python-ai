a = int(input("Enter a number:"))
b = int(input("Enter another number:"))

choice = int(input(
    "Enter your choice:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n"))
while choice:
    if choice == 1:
        print(a+b)
        break
    if choice == 2:
        print(a-b)
        break
    if choice == 3:
        print(a*b)
        break
    if choice == 4:
        print(a/b)
        break
