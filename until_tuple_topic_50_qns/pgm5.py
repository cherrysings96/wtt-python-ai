# Check whether a number is divisible by 5 and 11.

x = int(input("Enter a number:"))

if x % 5 == 0 and x % 11 == 0:
    print(x, "is divisble by 5 and 11")
else:
    print(x, "IS NOT divisible by 5 and 11")
