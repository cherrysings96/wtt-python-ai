# hollow pyramid
for i in range(1, 5):
    for space in range(4-i):
        print(" ", end=" ")
    for j in range(2*i-1):
        if (i, j) in [(2, 1), (3, 1), (3, 2), (3, 3)]:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()
