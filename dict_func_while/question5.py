sentences="My name is Sherene Sherene is a girl."


words=sentences.split()
frequency={}
for word in words:
    if word in frequency:

        frequency[word]+=1
    else:
        frequency[word]=1

print(frequency)

for word,count in frequency.items():
    if count>1:
        print(word)


