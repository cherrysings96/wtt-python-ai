def factorial(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res


n = int(input("Enter a no.:"))
result = factorial(n)
print(result)
