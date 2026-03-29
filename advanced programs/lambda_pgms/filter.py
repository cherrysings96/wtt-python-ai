# Filter even numbers
numbers=[1,2,3,6,7,8]
is_even=list(filter(lambda x:x%2==0,numbers))
print(is_even)
# Filter odd numbers
odd=list(filter(lambda x:x%2!=0,numbers))
print(odd)
# Filter positive numbers
pos=list(filter(lambda x:x>0,numbers))
print(pos)
# Filter negative numbers
negative=list(filter(lambda x:x<0,numbers))
print(negative)
# Filter numbers greater than 5
moreThan5=list(filter(lambda x:x>5,numbers))
print(moreThan5)
# Filter strings with length > 3
strings=["apple","max","pear",""]
moreThan3=list(filter(lambda x:len(x)>3,strings))
print(moreThan3)
# Remove empty strings
removeEmpty=list(filter(None,strings))
print(removeEmpty)
# Filter multiples of 3
mul3=list(filter(lambda x:x%3==0,numbers))
print(mul3)
# Filter numbers less than 10
lessThan10=list(filter(lambda x:x<10,numbers))
print(lessThan10)
# Filter vowels from list
l=['a','b','c','d','A']
isVowel=list(filter(lambda x:x in 'aeiouAEIOU',l))
print(isVowel)