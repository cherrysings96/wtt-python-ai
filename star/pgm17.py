# plus star pattern

for i in range(1, 4):
    for j in range(3, 0, -1):
        if (i, j) in [(1, 1), (1, 3), (3, 1), (3, 3)]:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()
