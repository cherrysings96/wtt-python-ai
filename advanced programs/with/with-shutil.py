# # with shutil

# import shutil

# with open("f1.txt", "w+") as f:
#     f.write("Hello good morning how is your day")
#     f.seek(0)
#     data = f.read()
#     print(data)

# shutil.copy("f1.txt", "f2.txt")

# file=open("f2.txt","r")
# file.seek(0)
# data2=file.read()
# print(data2)

import shutil

with open("f1.txt","w+") as f:
    f.write("Hi I am having a good day")
    f.seek(0)
    data=f.read()
    print(data)

shutil.copy("f1.txt","f2.txt")

with open("f2.txt","r") as f2:
    print(f2.read())