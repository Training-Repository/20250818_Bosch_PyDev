import threading

'''
threading.Thread(group=None,
                 target=None,
                 name=None,
                 args=(),
                 kwargs={}
                 daemon=None)
'''

def do_some_work(val):
    
    print("doing some work in the thread.")
    print(f"echo: {val}")
    for _ in range(int(val)):
        print(".", end='')
    return 


val = "1000"

t = threading.Thread(target=do_some_work, args=(val,))
t.start()
print("Primary thread doing its own work")
t.join()
