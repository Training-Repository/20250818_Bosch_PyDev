# a =  10
# if (a != 10)
# if a != 10:
#     print("a is populated with 10")
# else:
#     print("a either has '0' or 'None'")


def TestRun(name=None):
    if not name:
        print("Name not specified")
    else:
        print(f"Hi {name}")

TestRun()
TestRun("Tom")