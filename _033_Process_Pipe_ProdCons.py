import multiprocessing
import random
import time

def Producer(conn):
    for _ in range(5):
        item = random.randint(1, 100)
        print(f"Producer: producing item '{item}'.")
        conn.send(item)
        time.sleep(random.uniform(0.1, 0.5))

    # Signal end of interaction to consumer with a poison pill
    conn.send(None)
    conn.close()

def Consumer(conn):
    while True:
        item = conn.recv()
        if item is None:
            break
        print(f"Consumer: consuming item '{item}'.")
        time.sleep(random.uniform(0.1, 0.5))


def Main():
    prod_conn, cons_conn = multiprocessing.Pipe()

    p1 = multiprocessing.Process(target=Producer, args=(prod_conn,))
    p2 = multiprocessing.Process(target=Consumer, args=(cons_conn,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("All Done!")

# print(f"{__name__ = }")

if __name__ == "__main__":
    Main()
# elif __name__ == "__mp_main__":
#     print("This is a child process")