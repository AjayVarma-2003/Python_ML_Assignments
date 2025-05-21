# Problem Statement - Write a program which contains filter(), map(), and reduce() in it. Python application which contains one list of numbers
#                     which are accepted from user. Filter should filter out all prime numbers. Map function will multiply each number by 2. Reduce
#                     will return Maximum number from that numbers.

from functools import reduce

def CheckPrime(no):
    divisors = 0
    
    if(no <= 1):
        return False
    else:
        for i in range(1, no+1):
            if(no % i == 0):
                divisors = divisors + 1
    
    if(divisors > 2):
        return False
    else:
        return True
    
def MultBy2(no):
    return no * 2

def CheckMaximum(no1, no2):
    if(no1 > no2):
        return no1
    else:
        return no2

def main():
    print("Enter number of elements : ")
    size = int(input())
    
    data = []
    print("Enter numbers : ")
    for i in range(size):
        no = int(input())
        data.append(no)
        
    print("Entered number list is : ",data)
    
    Fdata = list(filter(CheckPrime, data))
    print("Data after filter is : ",Fdata)
    
    Mdata = list(map(MultBy2, Fdata))
    print("Data after map is : ",Mdata)
    
    Rdata = reduce(CheckMaximum, Mdata)
    print("Final output after reduce is : ",Rdata)

if __name__ == "__main__":
    main()