# Count frequency of characters in a string.

s = "Mississippi"
d = {}

for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1
print(d)
