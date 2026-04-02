#count the frequency of an input in the content of a file
f4=open("f4.txt","w+")
f4.write("I am a girl studying Python. I am learning Python.")
f4.seek(0)    
content=f4.read()
print(content)
word=input("Enter a word:")
count=content.count(word)
print(f"The word '{word}' appears {count} times in the file.")



