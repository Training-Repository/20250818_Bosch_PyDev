import ctypes
from multiprocessing import Process, Lock, Value

def example_function(shared_int, shared_long, shared_bool):
    with shared_int.get_lock():
        shared_int.value += 1

    with shared_long.get_lock():
        shared_long.value += 5

    # with shared_bool.get_lock():
    shared_bool.value = not shared_bool.value

    
if __name__ == "__main__":
    # Shared Integer, defaults to 0
    shared_int = Value('i', 0)  # 'i' stands for int type

    # Shared long integer
    shared_long = Value('l', 0)

    # Shared bool
    shared_bool = Value(ctypes.c_bool, False, lock=False)

    # a = [1, 2, 3, 4, 5]
    # b = [x**2        for x in a     if x%2 == 1]
    # print(a, b, sep="\n")

    processes = [Process(target=example_function, args=(shared_int, shared_long, shared_bool))  for _ in range(5)]
    print(f"{type(processes) = }")
    print(f"{processes = }")

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print(f"{shared_int.value = }")
    print(f"{shared_long.value = }")
    print(f"{shared_bool.value = }")
