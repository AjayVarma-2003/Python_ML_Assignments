import os

def main():
    print("Enter the name of file : ")
    filename = input()

    flag = os.path.exists(filename)
    if(flag == True):
        print("This file exists in current directory.")
    else:
        print("There is no such file available in current directory.")

if __name__ == "__main__":
    main()