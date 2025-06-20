import os

def main():
    print("Enter the name of file : ")
    FileName = input()

    ret = os.path.exists(FileName)
    if(ret == True):
        fobj = open(FileName, "r")
        data = fobj.read()
        print("Data of file is : ", data)
    else:
        print("There is no such file in current directory.")

if __name__ == "__main__":
    main()