a = "Python programming"
print(a[0])
print(a[3])
print(a[-1])

print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.replace("Python", "Java"))

b = [10, "Hello", 3.5, True]

c = [1, 2, 3]
print(c)

d = list((1, 2, 4))
print(d)

e = [10, 20, 30, 40, 50]
print(e[1:4])
print(e[:3])
print(e[2:])

f = [10, 20, 30]
f[1] = 33

print(f)

g = [1, 2, 3]
g.append(4)

print(g)

g.insert(1, 5)
print(g)

g.remove(3)
print(g)

g.pop(-1)
print(g)

g.clear()
print(g)

print(len(g))

h = [1, 3, 5, 6, 7]
print(len(h))

for i in h:
    print(i)

j = [3, 4, 2, 1]

j.reverse()
print(j)
j.sort()
print(j)

j.sort(reverse="True")  # desc
print(j)

print(max(j))
print(min(j))
print(sum(j)/len(j))
