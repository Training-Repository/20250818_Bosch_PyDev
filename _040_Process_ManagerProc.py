from multiprocessing import Manager, Process

def worker(shared_dict, shared_list):
    shared_dict['count'] += 1
    [shared_list.append(x)    for x in range(2)]



if __name__ == "__main__":
    manager = Manager()

    shared_dict = manager.dict({'count': 0})
    shared_list = manager.list()

    processes = []

    for _ in range(5):
        p = Process(target=worker, args=(shared_dict, shared_list))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"{dict(shared_dict) = }")
    print(f"{list(shared_list) = }")
