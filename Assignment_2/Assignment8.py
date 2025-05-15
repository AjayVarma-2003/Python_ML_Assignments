# Problem Statement - Write a program which accepts one number and display below pattern.
# Input : 5
# Output : 1
#          1 2
#          1 2 3
#          1 2 3 4
#          1 2 3 4 5

def display(num):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(j, end = " ")
        print()

def main():
    print("Enter the number : ")
    no = int(input())
    
    display(no)

if __name__ == "__main__":
    main()