from threading import Semaphore, BoundedSemaphore

def RegSemaphore_test():
    s1 = Semaphore(5); print(s1._value)
    s1.acquire(); print(s1._value)
    s1.acquire(); print(s1._value)
    s1.acquire(); print(s1._value)
    s1.acquire(); print(s1._value)
    s1.acquire(); print(s1._value)
    s1.release(); print(s1._value)
    s1.acquire(timeout=5); print(s1._value)

    s1.release(); print(s1._value)
    s1.release(); print(s1._value)
    s1.release(); print(s1._value)
    s1.release(); print(s1._value)
    s1.release(); print(s1._value)
    s1.release(); print(s1._value)
    s1.release(); print(s1._value)

    s1.acquire(timeout=5); print(s1._value)
    s1.acquire(timeout=5); print(s1._value)
    s1.acquire(timeout=5); print(s1._value)
    s1.acquire(timeout=5); print(s1._value)
    s1.acquire(timeout=5); print(s1._value)
    s1.acquire(timeout=5); print(s1._value)
    s1.acquire(timeout=5); print(s1._value)


def BoundedSemaphore_test():
    s1 = BoundedSemaphore(5); print(s1._value)
    s1.acquire(); print(s1._value)
    s1.acquire(); print(s1._value)
    s1.release(); print(s1._value)
    s1.release(); print(s1._value)
    s1.release(); print(s1._value)
    s1.release(); print(s1._value)


# RegSemaphore_test()
BoundedSemaphore_test()
