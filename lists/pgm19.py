# " of student names and check if a particular name exists in the list

a = ["cindy", "sherene", "amina", "rakhi"]

b = input("Enter the name you want to search:")

if b in a:
    print(b, "is in the list")
else:
    print("not present")
