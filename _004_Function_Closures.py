# s1 = "Global String"

# def Outer(num):

#     def Inner():
#         s1 = "Inner String"
#         print(f"Inner --> {s1}, {num}")

#     # Inner()

#     s1 = "Outer String"
#     print(f"Outer --> {s1}")
#     return Inner

# fn1 = Outer(10)
# fn2 = Outer(20)
# fn3 = Outer(30)


# fn1()
# fn2()
# fn3()

# print(f"Global --> {s1}")

###############################################

def PowerOf(exp):
    def calc(num):
        return num**exp
    return calc

p0 = PowerOf(0)
p1 = PowerOf(1)
p2 = PowerOf(2)
p3 = PowerOf(3)

print(p0(750))
print(p1(750))
print(p2(2))
print(p3(2))

lst = []
for i in range(5):
    lst.append(PowerOf(i))

print(lst[3](2))