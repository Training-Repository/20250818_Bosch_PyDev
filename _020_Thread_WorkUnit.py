import threading

'''
threading.Thread(group=None,
                 target=None,
                 name=None,
                 args=(),
                 kwargs={}
                 daemon=None)
'''


class FibonacciThread(threading.Thread):
    def __init__(self, num):
        super().__init__()      # Has to be the first line in the overridden initialiser
        self.num = num

    def run(self):
        fib = [0] * (self.num + 1)
        fib[0] = 0; print(f"{self.name} --> {fib[0]}")
        fib[1] = 1; print(f"{self.name} --> {fib[1]}")
        for i in range(2, self.num + 1):
            fib[i] = fib[i-1] + fib[i-2]
            print(f"{self.name} --> {fib[i]}")


#--------------------------------------------------------

fibTask1 = FibonacciThread(9)
fibTask2 = FibonacciThread(12)
fibTask1.start()
fibTask2.start()
fibTask1.join()
fibTask2.join()
