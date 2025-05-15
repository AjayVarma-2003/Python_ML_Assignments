# Problem Statement - Write a program which accept N numbers from user and store it into list. Accept one another number from user and
#                     return frequency of that number from list
# Input : Number of elements = 11
#         Input elements = 13 5 45 7 4 56 5 34 2 5 65
#         Element to search = 5
# Output : 3

def CheckFreq(values, num):
    result = 0
    
    for i in values:
        if i == num:
            result = result + 1
            
    return result

def main():
    print("Enter the number of elements : ")
    Size = int(input())
    
    data = []
    for i in range(Size):
        no = int(input())
        data.append(no)
        
    print("Enter the number to search : ")
    no1 = int(input())
        
    ret = CheckFreq(data, no1)
    
    print("Frequency of number is : ",ret)
        
if __name__ == "__main__":
    main()