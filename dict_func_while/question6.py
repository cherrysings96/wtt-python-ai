dic={'a':1,'b':2,'c':1,'d':3}
result={}

for key,value in dic.items():
    if value not in result:
        result[value]=[]
        result[value].append(key)
    else:
        result[value].append(key)
    
print(result)