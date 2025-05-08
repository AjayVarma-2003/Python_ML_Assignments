# Problem Statement - Write a program which contains one function named as Add() which accepts two numbers 
# from user and return addition of that two numbers.

def Add(num1, num2):
    result = num1 + num2
    return result

def main():
    print("Enter first number : ")
    no1 = int(input())
    
    print("Enter second number : ")
    no2 = int(input())
    
    ans = Add(no1, no2)
    
    print("Addition of numbers is : ",ans)
    
if __name__ == "__main__":
    main()