import time
import os 
from multiprocessing import Process,current_process

def sq(numbers):
    for num in numbers:
        time.sleep(0.5)
        res = num*num
        print(f"Square of {num} is {res}")
    #process_id = os.getpid() # returns the process id assigned to the process by the OS
    #print("Process_id:",process_id)
    
    process_name = current_process().name # returns the name of the current process that is runningon our machine
    print("Process_name:",process_name)
    

if __name__ == "__main__":

    processes = []
    numbers = range(100)
    for i in range(50):
        process = Process(target=sq,args=(numbers,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("Multiprocessing complete")
