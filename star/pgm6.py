for i in range(1, 5):
    for space in range(4-i, 0, -1):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
