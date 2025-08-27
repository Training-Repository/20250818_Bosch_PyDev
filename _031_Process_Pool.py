import multiprocessing
import time

# pool = multiprocessing.Pool(
#     processes=None,
#     initializer=None,
#     initargs=(),
#     maxtasksperchild=None
# )

def do_work(data):  ## Target
    time.sleep(4)
    return data**2

def start_process(): ## Initialiser
    print(f"Starting {multiprocessing.current_process().name}")


# ## MAP & MAP_ASYNC ##############################################
if  __name__ == "__main__":
    pool_size = multiprocessing.cpu_count() * 2

    print(f"{pool_size = }")

    pool = multiprocessing.Pool(
        processes=pool_size,
        initializer=start_process
    )

    inputs = list(range(10))

    # Synchronous
    outputs = pool.map(do_work, inputs)     # returns a list of the results
    print(f"{type(outputs) = }")
    print(f"Outputs (sync) --> {outputs}")

    # Asynchronous
    result = pool.map_async(do_work, inputs)    # returns an object of 'class MapResult'
    print(f"{type(result) = }")
    try:
        outputs = result.get(timeout=2)      # returns a list of the results
    except multiprocessing.TimeoutError as ex:
        print("Data still processing ...")
        outputs = result.get()
        print(f"Outputs (async) --> {outputs}")

    pool.close()
    pool.join()



## APPLY & APPLY_ASYNC ##############################################
if  __name__ == "__main__":
    pool_size = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(
        processes=pool_size,
        initializer=start_process
    )

    # Synchronous
    output = pool.apply(do_work, (7,))
    print(f"{output = }")

    ## Asynchronous
    result = pool.apply_async(do_work, (7,))
    output = result.get()
    print(f"{output = }")

    pool.close()
    pool.join()
