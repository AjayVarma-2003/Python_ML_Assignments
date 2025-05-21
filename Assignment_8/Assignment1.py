# Problem Statement - Design python application which creates two thread named as even and odd. Even
#                     thread will display first 10 even numbers and odd thread will display first 10 odd
#                     numbers.

import threading

def DisplayEven():
    result = []
    for i in range(2, 21, 2):
        result.append(i)
    print("First 10 even numbers are : ",result)

def DisplayOdd():
    result = []
    for i in range(1, 20, 2):
        result.append(i)
    print("First 10 odd numbers are : ",result)

def main():
    even = threading.Thread(target = DisplayEven)
    odd = threading.Thread(target = DisplayOdd)
    
    even.start()
    odd.start()
    
    even.join()
    odd.join()

if __name__ == "__main__":
    main()