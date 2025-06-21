import os

def main():
    print("Enter the name of file : ")
    filename = input()

    flag = os.path.exists(filename)
    if(flag == True):
        fobj = open(filename, "r")
        data = fobj.read()
        print("Data of file is : \n")
        print(data)
    else:
        print("There is no such file available in current directory.")

if __name__ == "__main__":
    main()