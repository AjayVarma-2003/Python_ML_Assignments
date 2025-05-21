# Problem Statement - Write a python program using multiprocessing. Process to square a list of numbers using multiple processes.

import multiprocessing
import os

def CalculateSquare(values):
    print("The process which is executing the code now is : ",os.getpid())
    result = []
    square = 1
    for i in values:
        square = i * i
        result.append(square)
    print("Square of numbers are : ",result)

def main():
    print("Enter number of elements : ")
    size = int(input())
    
    data = []
    print("Enter numbers : ")
    for i in range(size):
        no = int(input())
        data.append(no)
        
    print("List of numbers entered is : ",data)
        
    process1 = multiprocessing.Process(target = CalculateSquare, args = (data, ))
    process2 = multiprocessing.Process(target = CalculateSquare, args = (data, ))
    
    process1.start()
    process2.start()
    
    process1.join()
    process2.join()

if __name__ == "__main__":
    main()