# Problem Statement - Design python application which creates two threads as evenfactor and oddfactor. Both the thread accept one parameter as integer.
#                     EvenFactor thread will display addition of even factors of the number and OddFactor will display addition of odd factors of given
#                     number. After execution of both the thread gets compeleted main thread should display message as "exit from main".

import threading

def SumEvenFactors(num):
    sum = 0
    
    for i in range(1, num+1):
        if(num % i == 0):
            if(i % 2 == 0):
                sum = sum + i
                
    print("Addition of all even factors of number is : ",sum)

def SumOddFactors(num):
    sum = 0
    
    for i in range(1, num + 1):
        if(num % i == 0):
            if(i % 2 != 0):
                sum = sum + i
                
    print("Addition of all odd factors of number is : ",sum)

def main():
    print("Enter number : ")
    no = int(input())
    
    EvenFactor = threading.Thread(target = SumEvenFactors, args = (no,))
    OddFactor = threading.Thread(target = SumOddFactors, args = (no,))
    
    EvenFactor.start()
    OddFactor.start()
    
    EvenFactor.join()
    OddFactor.join()
    
    print("Exit from main menu.")

if __name__ == "__main__":
    main()