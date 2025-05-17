# Problem Statement - Write two lambda functions to calculate square and cube of number.

CalculateSqr = lambda A : (A ** 2)

CalculateCube = lambda A : (A ** 3)

def main():
    print("Enter the number : ")
    no = int(input())
    
    sqr = CalculateSqr(no)
    print("Square is : ",sqr)
    
    cube = CalculateCube(no)
    print("Cube is : ",cube)

if __name__ == "__main__":
    main()