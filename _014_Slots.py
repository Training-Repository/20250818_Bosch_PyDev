class MyClass:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = MyClass(10, 20)
print(obj.x)
print(obj.y)

try:
    obj.z = 30
except AttributeError as ex:
    print(f"{type(ex)} --> {ex}")


print(obj.__slots__)


del obj.x
print(obj.__slots__)
