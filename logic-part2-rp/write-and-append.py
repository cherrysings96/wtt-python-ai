file = open("data.txt", "w")
file.write("I am a developer.")
file.close()

file = open("data.txt", "a")
file.write(" I am working in Python.")
file.close()

file = open("data.txt", "r")
file.seek(0)
reading = file.read()
print(reading)
file.close()
