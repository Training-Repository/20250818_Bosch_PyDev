def greet():
    print("Hi there!")

def greetName(name):
    greeting = helper("Hello", name)
    print(greeting)

def helper(greeting, name):
    return f"{greeting} {name}!!"

def Test():
    greet()
    greetName("Ramakant")

print(f"{__name__ = }")

if __name__ == "__main__":
    Test()
