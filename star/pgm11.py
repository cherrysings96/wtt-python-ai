# hollow square
for i in range(1, 5):
    for j in range(1, 5):
        if (i, j) in [(2, 2), (2, 3), (3, 2), (3, 3)]:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()
