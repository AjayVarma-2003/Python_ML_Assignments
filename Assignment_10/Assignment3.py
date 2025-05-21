# Problem Statement - Write a program which contains filter(), map(), and reduce() in it. Python application which accpets one list of numbers.
#                     List contains numbers which accepted from user. Filter should filter out all such numbers which are greater than or equal
#                     to 70 and less than and equal to 90. Map function will increase the number by 10. Reduce will return product of all that numbers.

from functools import reduce

def Check(no):
    if(no >= 70 and no <=90):
        return True
    else:
        return False
    
def Increment(no):
    return no + 10

def Mult(no1, no2):
    return no1 * no2

def main():
    print("Enter number of elements : ")
    size = int(input())
    
    data = []
    print("Enter numbers : ")
    for i in range(size):
        no = int(input())
        data.append(no)
        
    print("Entered data is : ",data)
        
    Fdata = list(filter(Check, data))
    print("Data after filter is : ",Fdata)
    
    Mdata = list(map(Increment, Fdata))
    print("Data after map : ",Mdata)
    
    Rdata = reduce(Mult, Mdata)
    print("Final output using reduce is : ",Rdata)

if __name__ == "__main__":
    main()