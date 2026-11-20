#count the number of duplicate words in a file in a simple way
f5=open("f5.txt","w+")
f5.write("I am a girl studying Python. I am learning Python.") 
f5.seek(0) 
content=f5.read()
print(content)
data=content.lower().split()
print(data)
word_count={}
for word in data:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
print(word_count)
for word,count in word_count.items():
    if count>=2:
        print(word,count)
f5.close()