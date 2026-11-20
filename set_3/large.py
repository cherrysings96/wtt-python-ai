my_list = [3, 9, 6, 5, 2, 10]
largest = my_list[0]
for i in my_list:
    if i > largest:
        largest = i
print(f"Largest:{largest}")
