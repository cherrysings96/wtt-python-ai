data=['apple','orange','banana']
for index,value in enumerate(data,start=1):
    print(f"{index}:{value}")

data2=['appley','orangey','peary','fruity']
for index,value in zip(data,data2):
     print(f"{index}:{value}")

