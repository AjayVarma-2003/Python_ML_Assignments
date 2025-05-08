# Problem Statement - Write a program which accept number from user and print that number of "*" on screen.

def main():
    print("Enter number : ")
    no = int(input())
    
    for i in range(no):
        print("*")
    
if __name__ == "__main__":
    main()