def LoggedVersion(fn):
    def wrapper(*args, **kwArgs):
        print(f"Calling {fn.__name__}...")
        result = fn(*args, **kwArgs)
        print(f"Exiting {fn.__name__}...")
        return result
    return wrapper

@LoggedVersion
def SayHello():
    print("Hello")

@LoggedVersion
def SayHi():
    print("Hi")

@LoggedVersion
def add(a, b):
    return a + b

#-------------------------------------

SayHello()
SayHi()
print(add(5, 7))
print(add(b=2, a=1))
