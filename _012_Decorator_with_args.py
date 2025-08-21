# def repeat(n):
#     def decorator(fn):
#         def wrapper(*args, **kwArgs):
#             for _ in range(n):
#                 result = fn(*args, **kwArgs)
#             return result
#         return wrapper
#     return decorator

# @repeat(n=10)
# def greet(name):
#     print(f"Hello {name}!")


# #--------------------------------------

# greet("Ramakant")


####################################################

def log_with_level(level):
    def decorator(fn):
        def wrapper(*args, **kwArgs):
            print(f"[{level.upper()}] Calling {fn.__name__} with args: {args}, kwArgs: {kwArgs}")
            result = fn(*args, **kwArgs)
            print(f"[{level.upper()}] {fn.__name__} returned: {result}")
            return result
        return wrapper
    return decorator

# @decorator
@log_with_level(level="info")
def add(a, b):
    return a + b

# @decorator
@log_with_level(level="Debug")
def sub(a, b):
    return a - b


#--------------------------------

print(add(7, 5))
print(sub(7, 5))

