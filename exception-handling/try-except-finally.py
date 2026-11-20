try:
    n = 0
    result = 10/n
    print(result)
except ZeroDivisionError:
    print("We cannot divide a number by zero in Python!")
finally:
    print("Successfully handled error!")
