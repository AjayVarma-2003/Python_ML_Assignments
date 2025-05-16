# Problem Statement - Write a program which contains filter(), map(), and reduce() in it. Python application which
#                     contains one list of numbers. List contains the numbers which are accepted from user. Filter 
#                     should filter out all such numbers which are greater than or equal to 70 and less than or equal to
#                     90. Map function will increase each number by 10. Reduce will return product of all that numbers.
# Input : [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# filtered list : [76, 89, 86, 90, 70]
# mapped list : [86, 99, 96, 100, 80]
# final Output : 6538752000

from functools import reduce

def eligible(num):
    if num >= 70:
        return True

def Increase(num):
    return num + 10

def Mult(A, B):
    return A * B

def main():
    print("Enter number of elements : ")
    size = int(input())
    
    data = []
    for i in range(size):
        no = int(input())
        data.append(no)
        
    filtered_list = list(filter(eligible, data))
    print("List after filter : ",filtered_list)
    
    map_list = list(map(Increase, filtered_list))
    print("List after map : ",map_list)
    
    result = reduce(Mult, map_list)
    print("Output after reduce : ",result)

if __name__ == "__main__":
    main()