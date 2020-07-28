from threading import Thread
import time

# Because of the Global Interpreter Lock (GIL) of python
# Only one CPU is working effectively
# Other is is sleeping and wait for GIL

def countdown(n):
    while n > 0:
        n -= 1

COUNT = 50000000

t1 = Thread(target=countdown, args=(COUNT//2,))
t2 = Thread(target=countdown, args=(COUNT//2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print(end - start)