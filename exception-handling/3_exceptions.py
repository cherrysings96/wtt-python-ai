# 4. WAP that handles three different exceptions
try:
    a = int(input("Enter a denominator that is an integer:"))
    l = [1, 2]
    result = 10/a
    print(result)
    print(l[2])  # index 2 does not exist in the list
except ValueError:
    print("This is not an integer")
except ZeroDivisionError:
    print("Number cannot be a zero")
except IndexError:
    print("Index doesn't exist in the list")
else:
    print("No errors")
finally:
    print("Program complete")
