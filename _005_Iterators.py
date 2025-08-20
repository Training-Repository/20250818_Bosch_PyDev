# Inside a for loop
x = [1, 2, 3, 4, 5]
s = "Hello"

for i in x:
    print(i, end='-')
print("\n")

for c in s:
    print(c, end='-')
print("\n")

#------------------
print("-"*25)

it = iter(x)
for _ in range(len(x)):
    print(next(it), end='-')
print("\n")
# next(it) # <-- throws an exception (StopIteration) if called after having iterated on all the elements

#------------------
print("-"*25)

it = iter(x)
try:
    while True:
        print(next(it), end='-')
except StopIteration:
    print("-- <End of Data>")


# Check f obj is iterable

def IsIterable(obj):
    try:
        iter(obj)
        print("Iterable")
        return True
    except TypeError:
        print("Not an iterable")
        return False

y = ()
z = {}

print(f"{IsIterable(x) = }")
print(f"{IsIterable(y) = }")
print(f"{IsIterable(z) = }")


a = 10
print(f"{IsIterable(a) = }")


# Iterables (lists, sets, dictionaries, etc.)
#   collections of multiple elements/datapoints
#   support the '__iter__()' method

# Iterators
#   maintain the state of iteration i.e. are aware of the last iteration that has occurred, and thier current position in the iterable
#   support the '__iter__()' and the '__next__()' methods
