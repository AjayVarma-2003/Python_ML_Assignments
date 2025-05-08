# Problem Statement - Write a program which contains one function named ChkNum() which accepts one parameter as number.
# If number is even then it should display "Even number" otherwise display "Odd number" on console.

def ChkNum(num):
    if(num % 2 == 0):
        print("Even number")
    else:
        print("Odd number")

def main():
    print("Enter the number : ")
    no = int(input())
    
    ChkNum(no)
    
if __name__ == "__main__":
    main()