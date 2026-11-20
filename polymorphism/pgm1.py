class Calculator:

    def multiply(self, a=1, b=1, c=1, d=1):
        return a*b*c*d


c = Calculator()
print(c.multiply(2, 3))
print(c.multiply(2, 3, 4))
print(c.multiply(5))
