import multiprocessing
import time

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n%2 == 0 or n%3 == 0:
        return False
    i=5
    while i*i <= n:
        if n%i == 0 or n % (i+2) == 0:
            return False
        i+=6
        return True
    
def find_primes(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes

if __name__=="__main__":
    numbers = list(range(100_000_000,101_000_001))
    processes = 5
    chunk_size =len(numbers)//processes
    chunks = [numbers[i : i+chunk_size] for i in range(0,len(numbers),chunk_size)]
     
    pool = multiprocessing.Pool(processes=processes)
    start_time = time.monotonic()

    results = pool.map(find_primes,chunks)
    primes = []
    for r in results:
        primes += r

    pool.close()
    pool.join()

    end_time = time.monotonic()
    print(f"Found {len(primes):_} prime numbers"
          f" between {numbers[0]:_} and {numbers[-1]:_}"
          f" in {(end_time - start_time):.2f} secs")
     



