# Problem Statement - Write a program which contains one lambda function which accepts one parameter and return power of two.

CalculateSquare = lambda A : (A ** 2)

def main():
    print("Enter the number : ")
    no = int(input())
    
    result = CalculateSquare(no)
    print("The value of number with power of two is : ",result)

if __name__ == "__main__":
    main()