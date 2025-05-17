# Problem Statement - Accept number and print its factorial using for loop.

def main():
    print("Enter the number : ")
    no = int(input())
    
    result = 1
    for i in range(1, no + 1):
        result = result * i
        
    print("Factorial of ",no," is : ",result)

if __name__ == "__main__":
    main()