# Problem Statement - Write a program which display first 10 even numbers on screen.

def main():
    print("Enter how many even numbers do you want to display of screen : ")
    no = int(input())
    
    range_of_user = no * 2
    
    for i in range(2, range_of_user + 1, 2):
        print(i)
    
if __name__ == "__main__":
    main()