# Problem Statement - Print triangle pattern using nested loops.

def main():
    print("Enter number : ")
    no = int(input())
    
    for i in range(1, no + 1):
        print("*    " * i)
    
if __name__ == "__main__":
    main()