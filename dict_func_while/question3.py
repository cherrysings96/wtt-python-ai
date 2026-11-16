diction={'a':1,'b':2,'c':3,'d':1}
result={
}

for key,value in diction.items():
    if value not in result:
        result[value]=value
    
    else:
        continue

print(result)

