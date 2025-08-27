x = 10

print(type(x))
print(id((x)))

y = 20
print(id(y))

z = x
print(id(z))

x += 1
print(x, z)
print(id(x), id(z))

y += 1
print(id(y))

s1 = "Test"
print(s1[0])
# s1[0] = "B"
s1 = "Best"
