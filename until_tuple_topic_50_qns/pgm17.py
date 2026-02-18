n = 132
temp = n
reverse = 0

while (temp != 0):
    dig = temp % 10
    reverse = reverse*10+dig
    temp = temp//10

print(reverse)
