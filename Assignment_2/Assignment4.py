# Problem Statement - Write a program which accepts one number from user and returns addition of its factors.
# Input : 12
# Output : 16    (1 + 2 + 3 + 4 + 6)

def factorsAdd(num):
    result = 0
    
    for i in range(1, num):
        if(num % i == 0):
            result = result + i
            
    return result

def main():
    print("Enter the number : ")
    no = int(input())
    
    ret = factorsAdd(no)
    print("Addition of factors is : ",ret)

if __name__ == "__main__":
    main()