# 2. WAP that asks the user for an index position of a list and handles errors

try:
    l = [1, 2, 3]
    index = int(input("Enter an index to read the number:"))
    print(f"{l[index]} is the number at index {index}")
except IndexError:
    print("You have entered an invalid index!")
