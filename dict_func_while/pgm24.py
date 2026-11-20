# Function to check Armstrong number.
# n = 1535
n = 153
temp = n
cube = 0


def armstrong():
    global temp, n, cube
    while (temp != 0):
        dig = temp % 10
        cube = cube+pow(dig, 3)
        temp = temp//10
    if cube == n:
        print(n, "is an Armstrong number")
    else:
        print(n, "is not an Armstrong number")


armstrong()
