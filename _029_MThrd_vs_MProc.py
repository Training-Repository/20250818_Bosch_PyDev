# import threading

# def do_some_work(val):
#     print("doing some work in a thread")
#     print(f"{threading.current_thread().name}: {val}")
#     return

# val = "test"
# t = threading.Thread(target=do_some_work, args=(val,))
# t.start()
# t.join()


#-----------------------------------------------------------------


# import multiprocessing

# def do_some_work(val):
#     print("doing some work in a thread")
#     print(f"echo: {val}")
#     return

# if __name__ == "__main__":
#     val = "test"
#     t = multiprocessing.Process(target=do_some_work, args=(val,))       # args need to be pickle-able
#     t.start()
#     t.join()

# print(f"{__name__ = }")


## Picklable Objects
#   * None, True, False
#   * Integers, Floats, Complex
#   * Normal and Unicode strings
#   * Any collection, provided it contains only picklable objects
#   * Top level function 
#   * Classes with picklable attributes


#-----------------------------------------------------------------


# import multiprocessing
# import threading

# threading.Thread()
'''
threading.Thread(group=None,
                 target=None,
                 name=None,
                 args=(),
                 kwargs={}
                 daemon=None)
'''


# multiprocessing.Process()
'''
multiprocessing.Process(group=None,
                        target=None,
                        name=None,
                        args=(),
                        kwargs={}
                        daemon=None)
'''

## Daemon
# True: Parent process on exit will terminate all child daemon process
# False: Parent process will wait for the child Non-daemon process
# None: Will be inherited from the creating process
# 
# Daemon process is not allowed to create child processes 


#-----------------------------------------------------------------
