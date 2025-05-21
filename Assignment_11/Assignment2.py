# Problem Statement - Write a recursive funtion to calculate factorial of number.

fact = 1

def Factorial(num):
    global fact
    
    if(num >= 1):
        fact = fact * num
        num = num - 1
        Factorial(num)
        
    return fact

def main():
    print("Enter number : ")
    no = int(input())
    
    result = Factorial(no)
    print("Factorial of number is : ",result)

if __name__ == "__main__":
    main()