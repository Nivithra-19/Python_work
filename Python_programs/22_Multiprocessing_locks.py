"""A lock or mutex (from mutual exclusion) is a synchronization primitive that 
prevents state from being modified or accessed by multiple threads of execution at once.
In simple words a lock prevents the state of a value inside the current thread in our program to be modified by another thread until 
the current thread  completes executing.
"""


import time
from multiprocessing import Process , Lock, Value

def add_500(total,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        total.value += 5
        lock.release()

def sub_500(total,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        total.value -= 5
        lock.release()

if __name__ == "__main__":

    total = Value('i',500)
    print(total.value)
    lock = Lock()
    add_process = Process(target=add_500,args=(total,lock))
    sub_process = Process(target=sub_500,args=(total,lock))

    add_process.start()
    sub_process.start()

    add_process.join()
    sub_process.join()
    print(total.value)