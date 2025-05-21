# Problem Statement - Create python program that compares execution time of summing numbers from 1 to 10 million using normal function,
#                     threading, and multiprocessing.

import time
import threading
import multiprocessing

def Sum(no):
    sum = 0
    for i in range(1, no+1):
        sum = sum + i
    print("Sum of addition of all numbers from 1 to 1 million is : ",sum)

def main():
    star_time1 = time.time()
    Sum(10000000)
    end_time1 = time.time()
    print("Normal function execution took ",end_time1 - star_time1," sec time.")
    
    star_time2 = time.time()
    thread1 = threading.Thread(target = Sum, args = (10000000, ))
    thread1.start()
    thread1.join()
    end_time2 = time.time()
    print("Multithreading execution took ",end_time2 - star_time2," sec time.")
    
    star_time3 = time.time()
    process1 = multiprocessing.Process(target = Sum, args = (10000000, ))
    process1.start()
    process1.join()
    end_time3 = time.time()
    print("Multiprocessing execution took ",end_time3 - star_time3," sec time.")

if __name__ == "__main__":
    main()