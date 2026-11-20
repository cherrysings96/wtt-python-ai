
#copy one file f1's contents to another file f2 with with keyword

# f1=open("f1.txt","w")
# f1.write("hi I'm sherene")
# with open("f1.txt","r") as f1:
#     contents=f1.read()
#     print(contents)
# with open("f2.txt","w+") as f2:
#     f2.write(contents)
#     f2.seek(0)
#     contents2=f2.read()
#     print(contents2)

#check if word exists in a file

f3=open("f3.txt","w+")
f3.write("I am a girl studying Python.")
f3.seek(0)
lines=f3.read()
print(lines)
word=input("Enter a word:")
while True:
    if word in lines:
        print("Exists")
        break
    else:
        print("Does not exist")
        break
f3.close()






        