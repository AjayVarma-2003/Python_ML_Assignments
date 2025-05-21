# Problem Statement - Create a python program that uses multiprocessing pool to compute factorial of numbers in list.

import multiprocessing

def Factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

def main():
    print("Enter number of elements : ")
    size = int(input())
    
    data = []
    print("Enter elements")
    for i in range(size):
        no = int(input())
        data.append(no)

    print("List of entered numbers are : ",data)    

    result = []
    
    process = multiprocessing.Pool()
    result = process.map(Factorial, data)
    
    process.close()
    process.join()
    
    print("Factorial of each number of entered in list is : ",result)

if __name__ == "__main__":
    main()