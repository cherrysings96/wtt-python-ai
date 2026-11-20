# 1. Create a pgm for a simple calc-- handle invalid inputs

try:
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter one more number:"))
    c = int(input(
        "Enter your choice on the calculator(1.Add 2.Subtract 3.Multiply 4.Divide):"))

    if c == 1:
        result = num1+num2
    elif c == 2:
        result = num1-num2
    elif c == 3:
        result = num1*num2
    elif c == 4:
        result = num1/num2
    else:
        result = "Invalid choice"
except ValueError:
    print("You cannot enter strings or values other than numbers!")

except ZeroDivisionError:
    if c == 4 and num2 == 0:
        print("Cannot divide a number by zero!")
else:
    print(f"Result={result}")
finally:
    print("Successful program")
