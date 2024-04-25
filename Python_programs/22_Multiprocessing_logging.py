"""Logging is a built-in module that provides a flexible framework for emitting log messages from your application. 
Logging is essential for understanding what your code is doing, diagnosing issues, 
and monitoring its behavior in various environments. """

import time
import logging
from multiprocessing import Process, Lock, Value
from  multiprocessing import log_to_stderr, get_logger

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
    lock = Lock()
    
    log_to_stderr() 
    """log_to_stderr() sets up a basic logging configuration that sends log messages to the standard error stream. 
    Log messages will typically be displayed in the console where your Python script is running."""
    logger = get_logger()
    """getLogger() is a method used to create or retrieve a logger object.
    Logger objects are used to emit log messages from different parts of your code."""
    logger.setLevel(logging.INFO)
    add_process = Process(target=add_500,args=(total,lock))
    sub_process = Process(target=sub_500,args=(total,lock))

    add_process.start()
    sub_process.start()

    add_process.join()
    sub_process.join()
    print(total.value)