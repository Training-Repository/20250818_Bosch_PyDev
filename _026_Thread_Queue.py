import threading
from threading import Thread
from queue import Queue
import time
import random

# condition = threading.Condition()
# queue = []

def produce(queue):
    for _ in range(10):
        time.sleep(random.uniform(0.1, 0.5))    # Simulate production time
        item = random.randint(1, 100)       # Generate random data, as the produce
        queue.put(item)
        print(f"Produced: {item}")
    print("Producer: poisoning the queue")
    queue.put(None)

def consume(queue):
    while True:
        item = queue.get()
        if item is None:
            print("Consumer: Nothing more to wait for")
            break
        print(f"[{threading.current_thread().name}] Consumed: {item}")
        queue.task_done()
        time.sleep(random.uniform(0.1, 0.5))    # Simulate item consumption time

def random_func():
    global queue
    queue.clear()

def main():
    queue = Queue()
    producer_thread = threading.Thread(target=produce, args=(queue,))
    consumer_thread_1 = threading.Thread(target=consume, name="Cons_1", args=(queue,))
    # consumer_thread_2 = threading.Thread(target=consume, name="Cons_2", args=(queue,))

    producer_thread.start()
    consumer_thread_1.start()
    # consumer_thread_2.start()

    producer_thread.join()
    consumer_thread_1.join()
    # consumer_thread_2.join()





# queue = Queue()
# t1 = Thread(target=, args=(queue,))
# t2 = Thread(target=, args=(queue,))


if __name__ == "__main__":
    main()

