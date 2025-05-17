# Problem Statement - Accept list of numbers and use reduce() (from functools) to find product of all numbers.

from functools import reduce

def Mult(A, B):
    return A * B

def main():
    print("Enter the number of elements : ")
    size = int(input())
    
    data = []
    print("Enter the numbers : ")
    for i in range(size):
        no = int(input())
        data.append(no)
        
    result = reduce(Mult, data)
    print("Product : ",result)

if __name__ == "__main__":
    main()