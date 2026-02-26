# Find missing number in list of 1 to N.
list = [1, 2, 3, 5]
n = 5


total = n*(n+1)/2
sum_of_list = sum(list)

missing_number = total - sum_of_list
print(missing_number)
