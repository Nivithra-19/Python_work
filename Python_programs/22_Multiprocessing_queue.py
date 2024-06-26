"""In Python's multiprocessing module, the Queue class provides a way to share data between processes safely.
"""

from multiprocessing import Process, Queue

def square(numbers,queue):
    for i in numbers:
        queue.put(i**2)

def cube(numbers,queue):
    for i in numbers:
        queue.put(i**3)


if __name__ == "__main__":
    
    numbers = range(5)
    queue = Queue()

    square_process = Process(target=square,args=(numbers,queue))
    cube_process = Process(target=cube,args=(numbers,queue))

    square_process.start()
    cube_process.start()

    square_process.join()
    cube_process.join()

    while not queue.empty():
        print(queue.get())