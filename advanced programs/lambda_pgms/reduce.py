from functools import reduce
#  Find sum of list
num=[1,2,3,4]
result=reduce(lambda x,y:x+y,num)
print(result)

# Find product of list
result2=reduce(lambda x,y:x*y,num)
print(result2)

# Find maximum number
maximum=reduce(lambda x,y:x if x>y else y,num)
print(maximum)

#  Find minimum number
minimum=reduce(lambda x,y:x if x<y else y,num)
print(minimum)

# Sum with initial value
sumWithInitial=reduce(lambda x,y:x+y,num,10)
print(sumWithInitial)

# Multiply with initial value
mulWithInitial=reduce(lambda x,y:x*y,num,10)
print(mulWithInitial)

# Concatenate strings
strings=['hi','there']
print(reduce(lambda x,y:x+y,strings))

# Count total characters
print(reduce(lambda x,y:len(x)+len(y),strings))

# Find largest string
print(reduce(lambda x,y:x if len(x)>len(y) else y,strings))

# Subtract elements
print(reduce(lambda x,y:x-y,num))