# Problems Statement - Write a program which accept N numbers from user and store it into list. Return addition of all elements from the list.
# Input : Number of elements = 6
#         Input elements = 13 5 45 7 4 56
# Output : 130

def Addition(values):
    result = 0
    
    for i in values:
        result = result + i
        
    return result

def main():
    print("Enter number of elements : ")
    size = int(input())
    
    data = []
    for i in range(size):
        no = int(input())
        data.append(no)
        
    ret = Addition(data)
    
    print("Addition of all elements is : ",ret)

if __name__ == "__main__":
    main()