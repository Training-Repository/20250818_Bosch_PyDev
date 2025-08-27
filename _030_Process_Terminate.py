import multiprocessing
import time

def do_work():
    print("Starting do_work function")
    time.sleep(5)
    print("Finished do_work function")

if __name__ == "__main__":
    p = multiprocessing.Process(target=do_work)
    print(f"[Before Start] Process is alive: {p.is_alive()}")

    p.start()
    print(f"[Running] Process is alive: {p.is_alive()}")

    # time.sleep(1)
    time.sleep(6)
    p.terminate()
    p.join()
    print(f"[After Termination] Process is alive: {p.is_alive()}")

    print(f"Process Exit Code: {p.exitcode}")
    
## Exit Code
# '0': no error; normal return from process
# > 0 : error exit return value is error code
# < 0 :  process was killed by signal, multiplied by (-1) 


## Terminating a process
#   * Shared resources will be put in an inconsistent state, like locks, semaphores, pipe/queue
#   * 'finally' clauses and exit handlers will NOT be run
# Better apporach is a poison pill approiach, or an event trigger approach