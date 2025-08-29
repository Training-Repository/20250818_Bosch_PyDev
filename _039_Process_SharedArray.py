import ctypes
from multiprocessing import Process, Lock, Array

def example_function(shared_int_array, shared_long_array, shared_bool_array):
    with shared_int_array.get_lock():
        for i in range(len(shared_int_array)):
            shared_int_array[i] = i*2

    with shared_long_array.get_lock():
        for i in range(len(shared_long_array)):
            shared_long_array[i]  = i*3

    # with shared_bool.get_lock():
    for i in range(len(shared_bool_array)):
        shared_bool_array[i] = (i%2 == 0)

    
if __name__ == "__main__":
    # Shared Integer, defaults to 0
    shared_int_array = Array('i', 10)  # 'i' stands for int type

    # Shared long integer
    shared_long_array = Array('l', 5)

    # Shared bool
    shared_bool_array = Array(ctypes.c_bool, 7, lock=False)

    # a = [1, 2, 3, 4, 5]
    # b = [x**2        for x in a     if x%2 == 1]
    # print(a, b, sep="\n")

    processes = [Process(target=example_function, args=(shared_int_array, shared_long_array, shared_bool_array))  for _ in range(5)]
    print(f"{type(processes) = }")
    print(f"{processes = }")

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print(f"{list(shared_int_array) = }")
    print(f"{list(shared_long_array) = }")
    print(f"{list(shared_bool_array) = }")
