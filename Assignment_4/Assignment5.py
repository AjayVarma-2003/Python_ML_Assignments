# Problem Statement - Write a program which contains filter(), map(), and reduce() in it. Python application which
#                     contains one list of numbers. List contains the numbers which are accepted from user. Filter
#                     should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
#                     return Maximum number from that numbers.
# Input : [2, 70, 11, 10, 17, 23, 31, 77]
# filtered_list : [2, 11, 17, 23, 31]
# map_list : [4, 22, 34, 56, 62]
# Output : 62

from functools import reduce

def Chckprime(num):
    divisors = 0
    
    if(num == 2):
        return True
    elif(num <= 1):
        return False
    else:
        for i in range(1, num + 1):
            if(num % i == 0):
                divisors = divisors + 1
                
    if(divisors > 2):
        return False
    else:
        return True
    
def MultBy2(num):
    return num * 2

def CheckMax(A, B):
    if(A > B):
        return A
    else:
        return B

def main():
    print("Enter number of elements : ")
    size = int(input())
    
    data = []
    for i in range(size):
        no = int(input())
        data.append(no)
        
    filtered_list = list(filter(Chckprime, data))
    print("List after filter : ",filtered_list)
    
    map_list = list(map(MultBy2, filtered_list))
    print("List after map : ",map_list)
    
    result = reduce(CheckMax, map_list)
    print("Output of reduce is : ",result)

if __name__ == "__main__":
    main()