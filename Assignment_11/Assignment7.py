# Problem Statement - Write a recursive function to print following pattern.
# *
# * *
# * * *
# * * * *

def Display(num):
    if(num > 0):
        for i in range(1, num+1):
            print("* " * i)
            num = num - 1
        Display(num)

def main():
    print("Enter number : ")
    no = int(input())
    
    Display(no)

if __name__ == "__main__":
    main()