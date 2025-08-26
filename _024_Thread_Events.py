import threading

event = threading.Event()



# a client thread can wait for the flag to set
event.wait()        # Blocks the thread if the flag is False



# a server thread can set or reset the event
event.set()     # sets the flag to True
event.clear()   # resets the flag to False