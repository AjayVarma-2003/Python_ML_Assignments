# Problem Statement - Write a program which accepts one number from user and display below pattern.
# Input : 5
# Output : * * * * *
#          * * * *
#          * * *
#          * *
#          *

def display(num):
    for i in range(num):
        print("*    " * num)
        num = num - 1
        
def main():
    print("Enter the number : ")
    no = int(input())
    
    display(no)

if __name__ == "__main__":
    main()