# Problem Statement - Create a python program that starts 3 threads, each printing numbers from 1 to 5 with delay of 1 second. Use threading.thread.

import threading
import time

def display1(): 
    print("Output of function of first thread")
    for i in range(1, 6):
        print(i)
        
def display2():
    time.sleep(1)    # delays by 1 second after thread starts working
    print("Output of function of second thread ")
    for i in range(1, 6):
        print(i)
        
def display3():
    time.sleep(2)
    print("Output of function of third thread")
    for i in range(1, 6):
        print(i)

def main():
    thread1 = threading.Thread(target = display1)
    thread2 = threading.Thread(target = display2)
    thread3 = threading.Thread(target = display3)
    
    thread1.start()
    thread2.start()
    thread3.start()
    
    thread1.join()
    thread2.join()
    thread3.join()

if __name__ == "__main__":
    main()