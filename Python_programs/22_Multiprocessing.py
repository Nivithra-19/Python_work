"""Multiprocessing in Python allows you to run multiple processes concurrently, utilizing multiple CPU cores to 
improve performance. It's particularly useful for CPU-bound tasks that can be parallelized, like 
intensive calculations or data processing. Python's multiprocessing module provides classes and functions 
to create and manage multiple processes, each with its own memory space, allowing for efficient parallel execution of tasks."""

import multiprocessing 

def sq_sum(numbers):
    total = sum([num**2 for num in numbers])
    print(f"Sum of squares from {numbers=}:{total}")

if __name__=="__main__":
    numbers = [10,20,30,40,50,60,70,80,90,100]
    chunk1 = numbers[:5]
    chunk2 = numbers[5:]

    p1 = multiprocessing.Process(target=sq_sum,args=(chunk1,))
    p2= multiprocessing.Process(target=sq_sum,args=(chunk2,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()


