file = open("para2.txt", 'r')
data = file.read()
l = data.split()
count = 0
for i in l:
    count += 1
print(count)
file.close()
