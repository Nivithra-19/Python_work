"""In the multiprocessing module, a Pool represents a pool of worker processes.
 It's used to distribute tasks across multiple processes efficiently. The Pool class provides methods to apply functions 
 to multiple arguments in parallel, manage the worker processes, and handle their communication. 
 It's especially useful for scenarios where you need to perform the same operation on a large set of data concurrently, 
 such as applying a function to each item in a list or processing batches of data in parallel."""


import time
from multiprocessing import Pool

def sum_sq(number):
    s = 0
    for i in range(number):
        s += i*i
    return s

def sum_sq_mp(numbers):
    start_time = time.time()
    p = Pool()
    result = p.map(sum_sq,numbers)
    p.close()
    p.join()
    end_time = time.time() - start_time
    print(f"Procesing {len(numbers)} numbers took {end_time} using multiprocessing")

def sum_sq_sp(numbers):
    start_time = time.time()
    result= []
    for i in numbers :
        result.append(sum_sq(i))
    end_time = time.time() - start_time
    print(f"Procesing {len(numbers)} numbers took {end_time} using serial processing")


if __name__ == "__main__":
    numbers = range(10000)
    sum_sq_mp(numbers)
    sum_sq_sp(numbers)

""" write the following code in terminal to get the no. of coresin your machine's cpu
python
import os
os.cpu_count()"""