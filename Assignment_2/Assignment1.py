# Problem Statement - Create module named as Arithmatic which contains 4 functions as Add(), Sub(), Mult() and Div().
# All functions accepts two parameters as number and perform operation. Write a pyhton program which call all functions
# from arithmatic module by accepting the parameters from user.

import Arithmatic

def main():
    print("Enter firs number : ")
    no1 = int(input())
    
    print("Enter second number : ")
    no2 = int(input())
    
    ret = Arithmatic.Add(no1, no2)
    print("Addition of numbers is : ",ret)
    
    ret = Arithmatic.Sub(no1, no2)
    print("Substraction of number is : ",ret)
    
    ret = Arithmatic.Mult(no1, no2)
    print("Multiplication is : ",ret)
    
    ret = Arithmatic.Div(no1, no2)
    print("Division of numbers is : ",ret)

if __name__ == "__main__":
    main()