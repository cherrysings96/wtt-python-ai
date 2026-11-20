# 3. handle index error while accessing a list element

try:
    l = [1, 2, 3, 4, 5, 6]
    print(l[6])
except IndexError:
    print("That index does not exist in the specific list!")
