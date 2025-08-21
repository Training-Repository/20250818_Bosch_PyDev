#region Version 1
# def SayHello():
#     print("Hello")

# def SayHi():
#     print("Hi")

# # fn = SayHello

# # def wrapper():
# #     print("Calling SayHello...")
# #     fn()
# #     print("Exiting SayHello...")

# # SayHello = wrapper

# def LoggedVersion(fn):
#     def wrapper():
#         print("Calling SayHello...")
#         fn()
#         print("Exiting SayHello...")
#     return wrapper

# SayHello = LoggedVersion(SayHello)
# SayHi = LoggedVersion(SayHi)

#endregion

#region Version 2
# def LoggedVersion(fn):
#     def wrapper():
#         print("Calling SayHello...")
#         fn()
#         print("Exiting SayHello...")
#     return wrapper

# @LoggedVersion
# def SayHello():
#     print("Hello")
#endregion


#region Version 3
def LoggedVersion(fn):
    def wrapper():
        print(f"Calling {fn.__name__}...")
        fn()
        print(f"Exiting {fn.__name__}...")
    return wrapper


@LoggedVersion
def SayHello():
    print("Hello")

@LoggedVersion
def SayHi():
    print("Hi")

#endregion
##--------------------------------------------


SayHello()
# LoggedSayHello()
print("-"*20, "\n")
SayHi()