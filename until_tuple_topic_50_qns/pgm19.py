c = 0


def fib(a, b, n):
    while b <= n:
        c = a+b
        fib(c, b+1, n)
    return c


x = fib(0, 1, 3)
print(x)
