## Define Higher vs. Define Earlier ########################
def Bar():
    print("Bar")
    Baz()

def Foo():
    print("Foo")
    Bar()

def Start():
    print("Main")
    Foo()

def Baz():
    print("Baz")

Start()


print(f"{type(Baz)=}")
