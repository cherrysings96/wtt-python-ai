# Remove duplicates from a list without using set().

list = [1, 2, 3, 4, 5, 2, 3, 1]
newlist = []
for i in list:
    if i not in newlist:
        newlist.append(i)
print(newlist)
