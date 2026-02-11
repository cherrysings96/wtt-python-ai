for i in range(4, 0, -1):
    for space in range(4-i):
        print(" ", end=" ")
    for j in range(2*i-1):
        print("*", end=" ")
    print()
