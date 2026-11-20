a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

choice = input(
    "1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n\nEnter your choice:")

if (choice == "1"):
    print(a+b)
elif (choice == "2"):
    print(a-b)
elif (choice == "3"):
    print(a*b)
elif (choice == "4"):
    print(a/b)
else:
    print("Invalid choice")
