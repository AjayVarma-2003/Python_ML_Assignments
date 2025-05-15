# Problem Statement - Write a program which accept number from user and return addition of digits in that number
# Input : 5187934    Output : 37

def CountDigits(num):
    result = 0
    
    while num > 0:
        result = result + (num % 10)    # result = 0 + (5187934 % 10)= 0 + 4
        num = num // 10                 # num = (5187934 // 10) = 518793 and loop will continue to iterate.
        
    return result

def main():
    print("Enter any number : ")
    no = int(input())
    
    ret = CountDigits(no)
    
    print("Number of digits are : ",ret)

if __name__ == "__main__":
    main()