# Problems Statement - Write a program which accept N numbers from user and store it into list. Return Minimum number of list.
# Input : Number of elements = 4
#         Input elements = 13 5 45 7
# Output : 5

def ChckMin(values):
    result = values[0]
    
    for i in values:
        if i < result:
            result = i
            
    return result

def main():
    print("Enter the number of elements : ")
    Size = int(input())
    
    Data = []
    for i in range(Size):
        no = int(input())
        Data.append(no)
        
    ret = ChckMin(Data)
    
    print("Minimum number is : ",ret)

if __name__ == "__main__":
    main()