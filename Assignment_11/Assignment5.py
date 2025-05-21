# Problem Statement : Write a recursive function to count how many zeros are in given number.

sum = 0

def NumberOfZero(num):
    global sum
    
    if(num > 0):
        if(num % 10 == 0):
            sum = sum + 1
        num = num // 10
        NumberOfZero(num)
        
    return sum

def main():
    print("Enter number : ")
    no = int(input())
    
    result = NumberOfZero(no)
    print("Number of zero in digit are : ",result)

if __name__ == "__main__":
    main()