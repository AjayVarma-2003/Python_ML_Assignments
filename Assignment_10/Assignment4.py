# Problem Statement - Write a program which contains filter(), map(), and reduce() in it. Python application which contains list of numbers
#                     accepted from user. Filter should filter out all such numbers which are even. Map function will calculate its square.
#                     Reduce will return addition of all that numbers.

from functools import reduce

def CheckEven(no):
    if(no % 2 == 0):
        return True
    else:
        return False
    
def Square(no):
    return no ** 2

def Sum(no1, no2):
    return no1 + no2

def main():
    print("Enter number of elemets : ")
    size = int(input())
    
    data = []
    print("Enter then numbers : ")
    for i in range(size):
        no = int(input())
        data.append(no)
        
    print("Entered numbers are : ",data)
    
    Fdata = list(filter(CheckEven, data))
    print("Data after filter : ",Fdata)
    
    Mdata = list(map(Square, Fdata))
    print("Data after map : ",Mdata)
    
    Rdata = reduce(Sum, Mdata)
    print("Final output after reduce is : ",Rdata)

if __name__ == "__main__":
    main()