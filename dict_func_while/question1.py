dict1={"a":1,"b":2,"c":3}
dict2={"b":2,"c":5,"d":10}

result=dict1.copy()

for key,value in dict2.items():
    if key in result:
        result[key]=result[key]*value
    else:
        result[key]=value

print(result) 

