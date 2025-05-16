# Problem Statement - Write a program which contains one lambda function which accepts one parameter and return
#                     power of two.

CaleculateSqr = lambda A : (A ** 2)

def main():
    print("Enter the number : ")
    no = int(input())
    
    ret = CaleculateSqr(no)
    
    print("Square of number is : ",ret)

if __name__ == "__main__":
    main()