try:
    x = int(input("Enter a number:"))
    y = int(input("Enter a number other than zero:"))
    print(x/y)
except ValueError:
    print("One or both of the input is not an integer")
except ZeroDivisionError:
    print("The denominator is a zero which you have entered")
else:
    print("Success!")
