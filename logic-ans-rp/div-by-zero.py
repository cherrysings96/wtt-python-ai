# Write a Python program that takes two numbers as input and performs division.
#  Handle the case where the denominator is zero using exception handling.
# Example:
# Input: a = 10, b = 0
# Output: Cannot divide by zero
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"


# Example usage
a = 10
b = 0
result = divide(a, b)
print(result)  # Output: Cannot divide by zero
