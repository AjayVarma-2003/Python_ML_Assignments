# Problem Statement - Write a program which accepts one number from user and returns its factorial.

def Fact(num):
    result = 1
    
    for i in range(1, num + 1):
        result = result * i
        
    return result

def main():
    print("Enter the number : ")
    no = int(input())
    
    ret = Fact(no)
    print("Factorial is : ",ret)

if __name__ == "__main__":
    main()