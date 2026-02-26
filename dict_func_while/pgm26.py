# recursive function to calc factorial


def fact(f):
    if f == 0:
        return 1
    else:
        f = f * fact(f-1)
        return f


result = fact(6)
print(result)
