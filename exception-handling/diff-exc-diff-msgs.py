# create a program where different exceptions show different messages

try:
    a = int(input("Enter a denominator that is an integer:"))
    result = 10/a
    print(result)
except ValueError:
    print("This is not an integer")
except ZeroDivisionError:
    print("Number cannot be a zero")
else:
    print("No errors")
finally:
    print("Program complete")
