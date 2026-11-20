# Write a lambda to add 5 to a number
add=lambda x:x+5
print(add(5))

# Lambda to find the smaller of two numbers
smaller=lambda x,y:x if x<y else y
print(smaller(3,4))

# Lambda to return first character of a string
first=lambda x:x[0]
print(first("String"))

# Lambda to check even or odd
isEven=lambda x:"even" if x%2==0 else "odd"
print(isEven(22))

# Lambda to find maximum of two numbers
maximum=lambda x,y:max(x,y)
print(maximum(2,3))

# Lambda to convert string to uppercase
uppercase=lambda x:x.upper()
print(uppercase("string"))

# Lambda to find length of string
length=lambda x:len(x)
print(length("string"))

# Lambda to subtract two numbers
sub=lambda x,y:x-y
print(sub(3,5))

# Lambda to check positive or negative
isPos=lambda x:"positive" if x>0 else "negative"
print(isPos(-5))

# Lambda to cube a number
cube=lambda x:x**3
print(cube(3))

