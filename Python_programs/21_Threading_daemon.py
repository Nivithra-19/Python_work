"""DAEMON THREAD

In Python's threading module, a daemon thread is a thread that runs in the background and does not prevent the program
from exiting when all non-daemon threads have finished execution. In other words, daemon threads are threads that run 
intermittently in the background and automatically terminate when the program exits, regardless of their current state 
of execution.

Here are some key points about daemon threads:

Background Tasks: Daemon threads are commonly used for performing background tasks such as monitoring, cleanup, or 
maintenance activities. These tasks typically do not require explicit termination and can run as long as the program is running.

Automatically Terminated: When all non-daemon threads (also known as user threads) have finished execution 
and the main program exits, Python automatically terminates all daemon threads, regardless of their current state.
This behavior ensures that daemon threads do not prevent the program from exiting and do not leave resources or processes
running indefinitely.

Set Daemon Status: In Python's threading module, you can set a thread as a daemon thread by setting its 
daemon attribute to True before starting the thread. By default, threads created using the Thread class are not daemon threads.

Resource Cleanup: Since daemon threads are automatically terminated when the program exits, they are not suitable for tasks 
that require cleanup or graceful termination procedures. Daemon threads should be used for tasks that do not require explicit
shutdown procedures.

Example Use Cases: Daemon threads are commonly used for tasks such as background logging, periodic polling, 
monitoring system resources, or handling non-critical background tasks in applications.

"""


import threading
import time

def worker():
    counter = 0
    while True:
        time.sleep(1)
        counter += 1
        print(counter)
        
threading.Thread(target=worker,daemon=True).start()
input("Press enter to quit\n")
