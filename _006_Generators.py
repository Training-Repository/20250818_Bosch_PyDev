# for i in range(2, 101, 2):
#     print(i, end='-')
# print("\n")

# even_num = [n for n in range(2, 101, 2)]
# print(even_num)

# def SimpleGen():
#     # return values from 1 to 5, each time it's called
#     # return 1
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5

# def Test():
#     it = SimpleGen()
#     print(next(it), end=" ")
#     print(next(it), end=" ")
#     print(next(it), end=" ")
#     print(next(it), end=" ")
#     print(next(it), end=" ")
#     print(next(it), end=" ")

# Test()

##############################################
# Fibonacci Generator
def FibGen(n):
    """Generates a sequence of 'n' Fibonacci numbers"""
    a, b = 0, 1

    for i in range(n):
        yield a, i
        a, b = b, a+b

def Test():
    it = FibGen(10)

    try:
        while True:
            print(next(it))
    except StopIteration:
        print("Done")

Test()