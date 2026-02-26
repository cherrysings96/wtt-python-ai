# Write a Python program to check whether a number is prime.
n = 7
for i in range(2, n, 1):
    if (n % i) == 0:
        print("Not prime")
        break
    else:
        print("Prime")
        break
