import os

def main():
    print("Enter the name of file : ")
    FileName = input()

    ret = os.path.exists(FileName)
    if(ret == True):
        print("It is available in current directory.")
    else:
        print("This file is not available in current directory.")

if __name__ == "__main__":
    main()