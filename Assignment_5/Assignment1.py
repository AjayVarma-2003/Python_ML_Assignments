# Problem Statement - Write a program to accept two integers from the user and display their sum, difference, multiplication and division.

def Add(A, B):
    return A + B

def Subtract(A, B):
    return A - B

def Multiply(A, B):
    return A * B

def Division(A, B):
    return A / B

def main():
    print("Enter first number : ")
    no1 = int(input())
    
    print("Enter second number : ")
    no2 = int(input())
    
    result = Add(no1, no2)
    print("Sum : ",result)
    
    result = Subtract(no1, no2)
    print("Difference : ",result)
    
    result = Multiply(no1, no2)
    print("Product : ",result)
    
    result = Division(no1, no2)
    print("Division : ",result) 
    
if __name__ == "__main__":
    main()