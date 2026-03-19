# cubes of the digits of the number have to be equal to the original number
# 153,370,371,407

def is_armstrong(num):
    num_str = str(num)
    total = 0
    for digit in num_str:
        total += int(digit) ** 3

    return total == num


print(is_armstrong(153))
print(is_armstrong(191))
