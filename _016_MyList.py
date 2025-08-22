lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = lst1 + lst2
print(lst3)

class MyList:
    def __init__(self, series):
        self.data = list(series)

    def __add__(self, other):
        lst = self.data + other.data
        return MyList(lst)

    def __str__(self):
        return str(self.data)
    
    def __len__(self):
        return len(self.data)

l1 = MyList({1, 2, 3})
l2 = MyList((4, 5, 6))
l3 = l1 + l2
print(type(l3))
print(l3)

print(len(l3))

for val in lst3:
    print(val, end=" ")
print()

for val in l3:
    print(val, end=" ")
print()
