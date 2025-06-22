import os
import hashlib
import sys

def CheckSum(Files):
    fobj = open(Files, "rb")

    hobj = hashlib.md5()

    buffer = fobj.read(1024)

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def DirectoryTravel(DirectoryName):
    flag = os.path.isabs(DirectoryName)
    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)
    
    flag = os.path.exists(DirectoryName)
    if(flag == False):
        print("There is no such directory.")

    flag = os.path.isdir(DirectoryName)
    if(flag == False):
        print("There is no such directory.")

    for FolderName, SubFolders, FileNames in os.walk(DirectoryName):
        for File in FileNames:
            fname = os.path.join(FolderName, File)
            ret = CheckSum(fname)
            print("CheckSum of file is : ", ret)

def main():
    border = "-" * 54
    
    print(border)
    print(border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This is help section of script.")
            print("Type --u to get info of how to use the script.")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("This is the usage section of script.")
            print("Type following command to run the code.")
            print("python script.py DirectoryName")
        
        else:
            DirectoryTravel(sys.argv[1])

    else:
        print("Invalid number of arguments.")
        print("Type --h for help section.")
        print("Type --u for use section.")

    print(border)
    print(border)

if __name__ == "__main__":
    main()