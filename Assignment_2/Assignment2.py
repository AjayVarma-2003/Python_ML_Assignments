# Problem statement - Write a program which accepts one number and prints below pattern.
# Input : 5 
# output : * * * * *
#          * * * * *
#          * * * * *
#          * * * * *
#          * * * * *

def display(num):
    for i in range(num):
        print("*    " * num)

def main():
    print("Enter the number : ")
    no = int(input())
    
    display(no)

if __name__ == "__main__":
    main()