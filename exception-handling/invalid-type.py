# 2. handle invalid input when converting text to integer


try:
    string = input("Enter a string:")
    print(int(string))
except ValueError:
    print("Cannot convert that to an int")
