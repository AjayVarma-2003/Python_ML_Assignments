# Problem Statement - Write a program which accepts number from user and check whether that number is positive or 
# negative or zero.

def main():
    print("Enter the number : ")
    no = int(input())
    
    if(no < 0):
        print("Negative number")
    elif(no > 0):
        print("Positive number")
    else:
        print("Zero")
    
if __name__ == "__main__":
    main()