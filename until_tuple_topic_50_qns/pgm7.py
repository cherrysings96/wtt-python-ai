# Check whether a character is alphabet, digit, or special character

x = input("Enter an alphabet,digit,or special character:")
if x.isalpha():
    print("Alphabet")
elif x.isnumeric() or x.isdecimal() or x.__contains__("-"):
    print("Number")
else:
    print("Special character")
