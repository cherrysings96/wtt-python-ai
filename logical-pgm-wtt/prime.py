# a natural number greater than 1 that has no positive divisors other than 1 and itself
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


print(is_prime(7))
print(is_prime(10))
