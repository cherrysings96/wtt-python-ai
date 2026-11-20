file = open("para.txt", 'r')
file.seek(0)
lines = file.readlines()
print(lines)
count = 0
for i in lines:
    count += 1
print(f"The number of lines in this file is {count}.")

file.close()
