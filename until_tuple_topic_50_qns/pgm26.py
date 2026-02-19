def isprime(n):

    for i in range(2, n):
        if n % i == 0 or n == 2:
            return False
    return True


x = isprime(12)
print(x)
