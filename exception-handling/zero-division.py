# 1. write a program that handles division by zero error

try:
    # Code that might fail
    result = 10 / 0
except ZeroDivisionError:
    # Code that runs if the error happens
    print("You cannot divide by zero!")
