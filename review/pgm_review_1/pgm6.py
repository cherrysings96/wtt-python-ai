# Check whether a number is palindrome.

n = 121
temp = n
rev = 0
while temp != 0:
    dig = temp % 10
    rev = rev*10+dig
    temp = temp//10
if n == rev:
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")
