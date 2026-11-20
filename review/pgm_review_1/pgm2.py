# Reverse a string without using [::-1].


s = "Hello"
st = ""
l = list(s)
print(l)
l.reverse()
print(l)
for i in l:
    st = st+i
print(st)
