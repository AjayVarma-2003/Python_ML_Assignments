# Problem Statement - Write a program which contains one lambda function which accepts two arguments and return 
#                     its multiplication.

Mult = lambda A, B : (A * B)

def main():
    print("Enter first number : ")
    no1 = int(input())
    
    print("Enter second number : ")
    no2 = int(input())
    
    ret = Mult(no1, no2)
    
    print("Multiplication is : ",ret)

if __name__ == "__main__":
    main()