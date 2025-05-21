# Problem Statement - Write a recursive function to print numbers from 1 to N.

number = 1

def DisplayNumber(num):
    global number
    
    if(num >= 1):
        for i in range(1, num+1):
            print(i, end = " ")
            num = num - 1
        DisplayNumber(num)

def main():
    print("Enter number : ")
    no = int(input())
    
    DisplayNumber(no)

if __name__ == "__main__":
    main()