# Problem Statement - Design python application which two threads named as thread1 and thread2. Thread1 display 1 to 50 on screen and
#                     thread2 display 50 to 1 in reverse order on screen. After execution of thread1 gets completed then schedule thread2.

import threading

def display1():
    print("Output of thread1 is : ")
    for i in range(51):
        print(i)
        
def display2():
    print("Output of thread2 is : ")
    for i in range(50, 0, -1):
        print(i)

def main():
    thread1 = threading.Thread(target = display1,)
    thread2 = threading.Thread(target = display2,)
    
    thread1.start()
    thread1.join()
    
    thread2.start()
    thread2.join()
    
if __name__ == "__main__":
    main()