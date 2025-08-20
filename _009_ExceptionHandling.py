# def Foo(data):
#     print("Entering Foo")
#     if not isinstance(data, int):
#         raise TypeError("Provided data is of the incorrect type. We can process only integers.")
#     print("Exiting Foo")

# def Main(data):
#     print("Entering Main")
#     try:
#         Foo(data)
#     except (TypeError, StopIteration) as ex:
#         print("Handling the exception...")
#         print("Release resources and cleanup operations...")
#         raise
#     except ZeroDivisionError as ex:
#         print("Notify user to check the data source")
#     except Exception:
#         print("Unknown exceptions occurred")
    
#     print("Exiting Main")

# print("START")
# data = "Ten"
# Main(data)
# print("STOP")


class InvalidAgeError(ValueError):
    def __init__(self, message, code):
        self.message = message
        self.code = code
        super().__init__(self.message, self.code)

def AcceptAge(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative", 1001)
    elif age < 21:
        raise InvalidAgeError("Person needs to be at least 21 years old for membership", 1002)
    else:
        print("Updating age in database")

def someFunction():
    try:
        AcceptAge(25)
    except InvalidAgeError as ex:
        print(f"{type(ex)}: {ex.message} (Error code: {ex.code})")

someFunction()
