s = "String"
rev = ""
result = True
for ch in s:
    rev = ch+rev
if s.lower() == rev.lower():
    print(result)
else:
    print(not result)
