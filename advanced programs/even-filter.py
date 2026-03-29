numbers = [-1, 1, 2, 3, 4, 33]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

odd = list(filter(lambda y: y % 2 != 0, numbers))
print(odd)

pos = list(filter(lambda z: z > 0, numbers))
print(pos)
