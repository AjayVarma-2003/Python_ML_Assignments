# Problem Statement - Accept the list of integers from user and use the map() function to double each value.

def DoubleNum(num):
    return num * 2

def main():
    print("Enter number of elements : ")
    size = int(input())
    
    deta = []
    print("Enter numbers : ")
    for i in range(size):
        no = int(input())
        deta.append(no)
        
    result = list(map(DoubleNum, deta))
    print("Doubled list is : ",result)

if __name__ == "__main__":
    main()