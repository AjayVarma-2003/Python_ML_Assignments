# Problem Statement - Write a program to check whether number entered is even or odd.

def ChckEven(A):
    if(A % 2 == 0):
        return True
    else:
        return False

def main():
    print("Enter the number : ")
    no = int(input())
    
    ret = ChckEven(no)
    
    if(ret == True):
        print(no," is even number.")
    else:
        print(no," is odd number.")

if __name__ == "__main__":
    main()