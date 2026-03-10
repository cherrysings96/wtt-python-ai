try:
    # Convert input to a float to allow for decimals and trigger ValueError if needed
    x = float(input("Enter a number: "))

    # This will trigger ZeroDivisionError
    print(x / 0)

except (ZeroDivisionError, ValueError):
    print("Invalid input: You must enter a number, and it cannot be divided by zero.")
