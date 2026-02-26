l = [1, 2, 3, 4, 5]
count_e = 0
count_o = 0


def even_odd():
    global l, count_e, count_o
    print("The even numbers are:")
    for i in l:
        if i % 2 == 0:
            print(i)
            count_e += 1

    print("The odd numbers are:")
    for i in l:
        if i % 2 != 0:
            print(i)
            count_o += 1
    return count_e, count_o


e, o = even_odd()
print("There are", e, "even numbers")
print("There are", o, "odd numbers")
