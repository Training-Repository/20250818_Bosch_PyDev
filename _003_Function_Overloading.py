# def add1(a, b):
#     print("method 1")
#     return a + b

# def add2(a, b, c):
#     print("method 2")
#     return a + b + c

# def add3(a, b, c, d):
#     print("method 3")
#     return a + b + c + d

# def add(*data):
#     match len(data):
#         case 2:
#             return add1(*data)
#         case 3:
#             return add2(*data)
#         case 4:
#             return add3(*data)
#         case _:
#             print("No such method supported")

# ######################################################

# print(add(1, 2))
# print(add(1, 2, 3))
# print(add(1, 2, 3, 4))

# Function Signature
#   * Name of the function
#   * No. of args of the function
#   * Types of the args
#   * Sequence of the types
#   * Return type does NOT matter


# int   add(int x, int y);            --> add_i_i
# int   add(int x, int y, int z);     --> add_i_i_i
# int   add(int x, float y);          --> add_i_f
# int   add(float x, int y);          --> add_f_i
# float add(float x, int y);          --> add_f_i    # This is the same name s the one before it. Leads to name collision

# Name mangling/decoration


from multipledispatch import dispatch

@dispatch(int, int)
def add(a, b):
    print("method 1")
    return a + b

@dispatch(int, int, int)
def add(a, b, c):
    print("method 2")
    return a + b + c

@dispatch(int, int, int, int)
def add(a, b, c, d):
    print("method 3")
    return a + b + c + d

@dispatch(int, float)
def add(a, b):
    print("method 4")
    return a + b

@dispatch(str, str)
def add(a, b):
    print("method 5")
    return a + b


######################################################

print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 2, 3, 4))
print(add(1, 2.0))
print(add('1', '2'))
