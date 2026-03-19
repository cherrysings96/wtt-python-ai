try:
    a = int(input("Enter a number:"))
    b = int(input("Enter denominator number:"))
    c = a/b
    print(c)
except ValueError:
    print("Input an integer only!")
except ZeroDivisionError:
    print("The denominator cannot be zero!")
else:
    print("Program ran without errors!")
