# x star pattern

for i in range(1, 4):
    for j in range(3, 0, -1):
        if (i, j) in [(1, 2), (2, 1), (2, 3), (3, 2)]:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()
