# operations = []

# # Stage 1
# def double(num):
#     return num * 2

# # Stage 2
# def Increment_7(num):
#     return num + 7

# # Stage 3
# def PowerOf4(num):
#     return num ** 4

# operations.append(double)
# operations.append(Increment_7)
# operations.append(PowerOf4)

operations = []
operations.append(lambda num: num*2)
operations.append(lambda num: num+7)
operations.append(lambda num: num**4)

# Lambdas
#   one codeline
#   no loops
#   non-blocking
#   can use simple if-else 


#-----------------------------------------

# def Transform1(num):
#     res1 = double(num)
#     res2 = Increment_7(res1)
#     res3 = PowerOf4(res2)
#     return res3

def Transform2(num):
    res = num
    for op in operations:
        res = op(res)
    return res


# print(f"{Transform1(5) = }")
print(f"{Transform2(5) = }")


nextEven = lambda x: x+2 if x%2==0 else x+1
print(f"{nextEven(5) = }")
print(f"{nextEven(10) = }")

# Use-case: in the map, filter, reduce methods
