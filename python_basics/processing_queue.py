import multiprocessing as mp
import time

def sub_task(cond, q):
    name = mp.current_process().name
    print("Starting: ", name)
    while True:
        i = q.get()
        print("accept: ", i)


if __name__ == "__main__":
    cond = mp.Condition()
    q = mp.Queue()
    p1 = mp.Process(name='p1', target=sub_task, args=(cond, q))
    p1.daemon = True
    p1.start()

    for i in range(10):
        time.sleep(1)
        q.put(i)
