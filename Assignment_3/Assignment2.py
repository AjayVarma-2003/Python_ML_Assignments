# Problem Statement - Write a program which accept N numbers from user and store it into list. Return Maximum number from that list.
# Input : Number of element = 7
#         Input elements = 13 5 45 7 4 56 34
# Output : 56

def CheckMax(values):
    result = values[0]
    
    for i in values:
        if i > result:
            result = i
    
    return result

def main():
    print("Enter number of elements : ")
    size = int(input())
    
    Data = []
    for i in range(size):
        no = int(input())
        Data.append(no)
        
    ret = CheckMax(Data)
    
    print("Maximum number is : ",ret)

if __name__ == "__main__":
    main()