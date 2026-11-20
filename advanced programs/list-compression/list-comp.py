# 1. create a list of squares from one to ten
# 2. create a list of even numbers from one to 20
# 3. convert a list of strings to lowercase
# 4. create a list of numbers divisible by 3
# 5. replace negative numbers with 0

print([x**2 for x in range(1,11)])

print([x for x in range(1,21) if x%2==0])

print([x.lower() for x in ["HI","BYE"]])

print([x for x in range(1,11) if x%3==0])

print([0 if x<0 else x for x in range(-11,11) ]) #else condition gives difference in syntax than just if condition