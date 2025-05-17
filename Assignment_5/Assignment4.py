# Problem Statement - Accept three numbers from the user and print the largest using nested if-else statements.

def ChckMaximum(values):
    result = values[0]
    
    for i in values:
        if result < i:
            result = i
            
    return result

def main():
    print("Enter three numbers : ")
    
    data = []
    for i in range(3):
        no = int(input())
        data.append(no)
        
    ret = ChckMaximum(data)
    
    print("Largest number is : ",ret)

if __name__ == "__main__":
    main()