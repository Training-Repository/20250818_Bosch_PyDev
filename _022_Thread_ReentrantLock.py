import threading

lock:threading.Lock = None

gbl_data = 100


# Acquiring the lock for the first time
def Foo():
    print("Foo")
    global gbl_data
    if lock.acquire() is True:
        print("Foo: Acquired lock")
        gbl_data += 100
        Bar()
        lock.release()
        print("Foo: Releasing the lock")
    else:
        print("Foo: Failed to lock")


# Acquiring the lock for the second time
def Bar():
    print("Bar")
    global gbl_data
    if lock.acquire(timeout=5) is True:
        print("Bar: Acquired lock")
        gbl_data += 10
        lock.release()
        print("Bar: Releasing the lock")
    else:
        print("Bar: Failed to lock")


if __name__ == "__main__":
    lock = threading.Lock()
    t1 = threading.Thread(target=Foo)
    t1.start()
    t1.join()

    print("="*25, "\n")

    lock = threading.RLock()
    t2 = threading.Thread(target=Foo)
    t3 = threading.Thread(target=Foo)
    t2.start()
    t3.start()
    t2.join()
    t3.join()
