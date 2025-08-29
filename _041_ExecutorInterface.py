# import threading

# def sayHello():
#     print(f"Hello from {threading.current_thread().name}")
#     return

# p = threading.Thread(target=sayHello)
# p.start()
# p.join()


###############################################################

# import multiprocessing, os

# def sayHello():
#     print(f"Hello from {os.getpid()}")
#     return

# if __name__ == "__main__":
#     p = multiprocessing.Process(target=sayHello)
#     p.start()
#     p.join()

###############################################################


from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def sayHello(name):
    print(f"Hello from {name}")
    return

if __name__ == "__main__":


    MyExecutor = ThreadPoolExecutor
    executor1 = MyExecutor(max_workers=2)
    # future = executor1.submit(sayHello, "Manish")
    # future.result()

    names = ("Manish", "Abhijeet")
    futures = [executor1.submit(sayHello, f"Thread {names[i]}") for i in range(2)]
    for future in futures:
        future.result()

    executor1.shutdown(wait=True)

    #---------------------------------------------------

    MyExecutor = ProcessPoolExecutor
    executor2 = MyExecutor(max_workers=2)
    # future = executor2.submit(sayHello, "Abhijeet")
    # future.result()

    names = ("Pravin", "Ramakant")
    futures = [executor2.submit(sayHello, f"Process {names[i]}") for i in range(2)]
    for future in futures:
        future.result()
    executor2.shutdown(wait=True)

    #-------------------------------------------------

    # def PushDataToDb():
    #     pass

    with ProcessPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(sayHello, f"Process {names[i]}") for i in range(2)]
        for future in futures:
            future.result()

            # future.add_done_callback(PushDataToDb)
            # future.cancel()
            # future.cancelled()
            # future.done()
            # future.exception()
 
    