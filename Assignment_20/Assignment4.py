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

    return Result

def DeleteDuplicate(path):
    MyDict = DirectoryTravel(path)

    Check = lambda X: (len(X) > 1)

    Result = list(filter(Check, MyDict.values()))

    fobj = open("Log.txt", "w")
    fobj.write("Deleted files are : \n")

    Count = 0
    cnt = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if(Count > 1):
                fobj.write(str(subvalue) + "\n")
                cnt += 1
                os.remove(subvalue)
        Count = 0     # resetting value.

    print("Total deleted files are : ", cnt)

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
            DeleteDuplicate(sys.argv[1])

    else:
        print("Invalid number of arguments.")
        print("Type --h for help section.")
        print("Type --u for use section.")

    print(border)
    print(border)

if __name__ == "__main__":
    main()