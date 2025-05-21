# Problem Statement - Design python application which creates two threads as evenlist and oddlist. Both threads accept list of integers as parameters.
#                     Evenlist thread add all even elements from input list and display addition. Oddlist thread add all odd elements from input list
#                     and display addition.

import threading

def SumEven(values):
    sum = 0
    
    for i in values:
        if(i % 2 == 0):
            sum = sum + i
            
    print("Sum of all even numbers from this list is : ",sum)

def SunOdd(values):
    sum = 0
    
    for i in values:
        if(i % 2 != 0):
            sum = sum + i
            
    print("Sum of all odd numbers from this list is : ",sum)

def main():
    print("Enter number of elements : ")
    size = int(input())
    
    data = []
    print("Enter numbers : ")
    for i in range(size):
        no = int(input())
        data.append(no)
        
    Evenlist = threading.Thread(target = SumEven, args = (data, ))
    Oddlist =  threading.Thread(target = SunOdd, args = (data, ))
    
    Evenlist.start()
    Oddlist.start()
    
    Evenlist.join()
    Oddlist.join()

if __name__ == "__main__":
    main()