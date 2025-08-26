'''
# NOT executable code
# Only to demonstrate the skeletal flow 


from threading import Condition

cond = Condition()

# Consume one item
cond.acquire()
while not an_item_is_available():
    cond.wait()
get_an_available_item()
cond.release()


# Produce and item
cond.acquire()
make_an_item_available()
cond.notify()
cond.release()
'''


import threading
import random
import time

class ProducerConsumer:
    def __init__(self):
        self.condition = threading.Condition()
        self.queue = []

    def produce(self):
        for _ in range(10):
            item = random.randint(1, 100)       # Generate random data, as the produce
            with self.condition:
                self.queue.append(item)
                print(f"Produced: {item}")
                self.condition.notify()             # Notify any consumers (who are waiting) that a new item is avaialble
            time.sleep(random.uniform(0.1, 0.5))    # Simulate production time

    def consume(self):
        for _ in range(10):
            with self.condition:
                while not self.queue:
                    self.condition.wait()
                item = self.queue.pop(0)
                print(f"Consumed: {item}")
            time.sleep(random.uniform(0.1, 0.5))    # Simulate item consumption time

def main():
    pc = ProducerConsumer()
    producer_thread = threading.Thread(target=pc.produce)
    consumer_thread = threading.Thread(target=pc.consume)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()


if __name__ == "__main__":
    main()