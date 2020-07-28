from multiprocessing import Process, Queue
import os

# 1.kill by pid on the console won't end the subprocess
#   using kill -9 -<group_id> instead


def long_runing_proc(q):
    print("*** setup subprocess: ", os.getpid())
    while True:
        com = q.get()
        print("accepted command: ", com)


if __name__ == "__main__":
    print("*** main process: ", os.getpid())
    q = Queue()

    p = Process(target=long_runing_proc,
                args=(q,),
                daemon=True)
    p.start()

    while True:
        com = input("input command: ")
        q.put(com)
        if com == "exit":
            print("quit")
            break
        if com == "exception":
            raise Exception("generate exception")
