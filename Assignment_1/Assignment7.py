# Problem statment - Write a program which contains one function that accept one number from user and returns
# true if number is divisible by 5 and false if not.

def ChkDivisibility(num):
    if(num % 5 == 0):
        return True
    else:
        return False

def main():
    print("Enter the number : ")
    no = int(input())
    
    ret = ChkDivisibility(no)
    
    print("Is number divisible by 5 : ",ret)
    
if __name__ == "__main__":
    main()