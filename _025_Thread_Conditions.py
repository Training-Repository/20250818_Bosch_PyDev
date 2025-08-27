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
        for _ in range(20):
            item = random.randint(1, 100)       # Generate random data, as the produce
            with self.condition:
                self.queue.append(item)
                print(f"Produced: {item}")
                self.condition.notify()             # Notify any consumers (who are waiting) that a new item is avaialble
            time.sleep(random.uniform(0.1, 0.5))    # Simulate production time

    def consume(self):
        ## Unconditional execution to process 10 items
        # cntr = 0
        # while cntr < 10:
        #     if not self.queue:
        #         continue
        #     item = self.queue.pop(0)
        #     print(f"Consumed: {item}")
        #     cntr += 1
        for _ in range(10):
            with self.condition:
                while not self.queue:
                    self.condition.wait()
                item = self.queue.pop(0)
                if threading.current_thread().name == "Cons_1":
                    print("\t", end='')
                else:
                    print("\t\t\t\t\t", end='')
                print(f"[{threading.current_thread().name}] Consumed: {item}")
            time.sleep(random.uniform(0.1, 0.5))    # Simulate item consumption time

def main():
    pc = ProducerConsumer()
    producer_thread = threading.Thread(target=pc.produce)
    consumer_thread_1 = threading.Thread(target=pc.consume, name="Cons_1")
    consumer_thread_2 = threading.Thread(target=pc.consume, name="Cons_2")

    producer_thread.start()
    consumer_thread_1.start()
    consumer_thread_2.start()

    producer_thread.join()
    consumer_thread_1.join()
    consumer_thread_2.join()


if __name__ == "__main__":
    main()