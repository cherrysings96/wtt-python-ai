# l=[-5,0,5] #zero and anything less than it is considered false, positives are considered true
# print(any(l)) #if any value is true returns true

# print(any(i>0 for i in l))
# print(all(i>0 for i in l)) #if all values are true returns true

p=[True,True,True]
print(any(p))
print(all(p))

print(any(not(i) for i in p))
print(all(not(i) for i in p))