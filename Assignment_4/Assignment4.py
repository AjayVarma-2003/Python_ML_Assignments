# Problem Statement - Write a program which contains filter(), map(), and reduce() in it. Python application which
#                     contains one list of numbers. List contains numbers which are accepted by user. Filter should
#                     filter out all such numbers whihc are even. Map function will calculate its square. Reduce will
#                     return addition of all that numbers.
# Input : [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# filtered list = [2, 4, 4, 2, 8, 10]
# map_list = [4, 16, 16, 4, 64, 100]
# Output : 204

from functools import reduce

def Chckeven(num):
    if(num % 2 == 0):
        return True
    
def square(num):
    return num ** 2

def Sum(A, B):
    return A + B

def main():
    print("Enter number of elements : ")
    size = int(input())
    
    data = []
    for i in range(size):
        no = int(input())
        data.append(no)
        
    filter_list = list(filter(Chckeven, data))
    print("List after list : ",filter_list)
    
    map_list = list(map(square, filter_list))
    print("List after map : ",map_list)
    
    result = reduce(Sum, map_list)
    print("Output of reduce : ",result)

if __name__ == "__main__":
    main()