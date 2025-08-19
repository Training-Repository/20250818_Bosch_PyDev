#region Define Higher vs. Define Earlier ########################
# def Bar():
#     print("Bar")
#     Baz()

# def Foo():
#     print("Foo")
#     Bar()

# def Start():
#     print("Main")
#     Foo()

# def Baz():
#     print("Baz")

# Start()


# print(f"{type(Baz)=}")

#endregion


#region Args

# def SayHi():
#     print("Hi there")

# def Add(a, b, *others):         # Variable arguments
# # def Add(*others):
#     # print(f"{a = }")
#     # print(f"{b = }")
#     print(f"{type(others) = }, {others = }")

#     sum  = a + b
#     for val in others:
#         sum += val

#     return sum

# SayHi()

# print(f"{Add(1, 2)=}")          # Positional args
# # print(f"{Add(b=1, a=2)=}")      # Named args / Keyworded args

# # Packing / Unpacking
# lst1 = [10, 20, 30, 40, 50, 60]
# print(f"{Add(lst1[0], lst1[1]) = }")

# p, q = 5, 7
# print(f"{p = }")
# print(f"{q = }")

# m = lst1
# print(f"{type(m) = }")
# x, *_, z = lst1         # Unpacking the collection
# print(f"{x = }")
# print(f"{z = }")

# # print(f"{type(others) = }, {others = }")

# # LHS, RHS --> LeftHandSide, RightHandSide
# # L-value, R-Value --> 

# lst2 = [1, 2]
# print(f"{Add(*lst2)=}")     # Unpacking the collection into the arg list of 'Add'


# r = 10
# s = 20
# print(f"{Add(p, q)=}")
# print(f"{Add(p, q, r)=}")
# print(f"{Add(p, q, r, s)=}")

# lst1 = [10, 20]
# print(f"{Add(*lst1)=}")



# # lst3 = [10]
# # print(f"{type(lst3) = }")
# # tup1 = (10,)
# # print(f"{type(tup1) = }")

# # res = (10+20)/5
# # res = (10)


#####################################

# def PrintEmp(ceo, cto, *just_people, **others):
#     print(f"{ceo = }")
#     print(f"{cto = }")
#     for people in just_people:
#         print(f"{people = }")
#     for position, person in others.items():
#         print(f"{position} = '{person}'")

# PrintEmp("Tom", "Mark")             # Positional args
# print("-"*20, "\n")
# PrintEmp(cto="Tom", ceo="Mark")     # Named/Keyworded args
# print("-"*20, "\n")
# PrintEmp("Tom", "Mark", "Bob", "Jack")
# print("-"*20, "\n")
# PrintEmp(cto="Tom", ceo="Mark", director="Bob", cfo="Jim")
# print("-"*20, "\n")
# PrintEmp("Tom", "Mark", "Jack", "John", director="Bob", cfo="Jim")  # Keyworded Variable args

#endregion

#region Scopes

# LEGB --> Local, External, Global, BuiltIns

# s1 = "Global String"

# def Outer():
#     # global s1
#     s1 = "Outer String"

#     print(f"{type(globals())}, {globals() = }")
#     print(f"{type(locals())}, {locals() = }")

#     print(f"Global string in Outer --> {globals()['s1'] = }")


#     def Inner():
#         # global s1
#         # nonlocal s1
#         s1 = "Inner String"
#         print(f"Inner --> {s1}")

#     Inner()
#     print(f"Outer --> {s1}")

# Outer()

# print(f"Global --> {s1}")
#endregion


# region Comprehensions
# Used to create a new collection, given an existing collection or generator

fruits = ['apple', 'banana', 'custardapple', 'dragonfruit', 'kiwi']
bowl = []
for fr in fruits:
    if 'a' in fr:
        bowl.append(fr)

print(f"{bowl = }")

bowl = [fr       for fr in fruits          if 'a' in fr]
print(f"{type(bowl)}, {bowl = }")

bowl = {fr       for fr in fruits          if 'a' in fr}
print(f"{type(bowl)}, {bowl = }")

bowl = {fr:len(fr)       for fr in fruits          if 'a' in fr}
print(f"{type(bowl)}, {bowl = }")

bowl = tuple(fr       for fr in fruits          if 'a' in fr)
print(f"{type(bowl)}, {bowl = }")


nums = [1, 2, 3, 4, 5]
squares = [x**2 for x in nums]
print(f"{squares = }")