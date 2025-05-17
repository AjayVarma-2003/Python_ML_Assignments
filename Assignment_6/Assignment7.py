# Problem Statement - Accept 5 number from user. Find and print largest number.

def CheckMax(values):
    no = values[0]
    
    for i in values:
        if no < i:
            no = i
            
    return no

def main():
    data = []
    
    print("Enter 5 numbers : ")
    for i in range(5):
        no = int(input())
        data.append(no)
        
    result = CheckMax(data)
    
    print("Maximum number is : ",result)
    
if __name__ == "__main__":
    main()