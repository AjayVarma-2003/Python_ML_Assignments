import sys
import os
import hashlib

def Checksum(File):
    fobj = open(File, "rb")

    hobj = hashlib.md5()

    buffer = fobj.read(1024)

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def LogBook(Mydict):
    Count = 0

    Check = lambda X: len(X) > 1

    Ret = list(filter(Check, Mydict.values()))

    fobj = open("Log.txt", "w")
    
    for value in Ret:
        for subvalue in value:
            Count += 1
            if(Count > 1):
                fobj.write(str(subvalue) + "\n")

    fobj.close()

def DirectoryTravel(DirectoryName):
    Result = {}

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
            ret = Checksum(fname)
            
            if ret in Result:
                Result[ret].append(fname)
            else:
                Result[ret] = [fname]

    print(Result)

    LogBook(Result)

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