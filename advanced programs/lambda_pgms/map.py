# Square all elements in a list
numbers=[1,2,3]
result=list(map(lambda x:x**2,numbers))
print(result)

# Convert all numbers to string
result2=list(map(lambda x:str(x),numbers))
print(result2)

# Add 10 to each element
result3=list(map(lambda x:x+10,numbers))
print(result3)

# Multiply each element by 2
result4=list(map(lambda x:x*2,numbers))
print(result4)

# Convert all strings to uppercase
strings=["apple","orange","pear"]
result5=list(map(lambda x:x.upper(),strings))
print(result5)

# Find length of each string
result6=list(map(lambda x:len(x),strings))
print(result6)

# Add two lists element-wise
numbers2=[4,5,6]
result7=list(map(lambda x,y:x+y,numbers,numbers2))
print(result7)

# Convert list of floats to integers
floats=[1.1,1.2,1.3]
result8=list(map(int,floats))
print(result8)

# Get absolute values
negative=[-1,-2,-3]
result9=list(map(abs,negative))
print(result9)

# Add suffix to strings
print(list(map(lambda x:x+"_suffix",strings)))