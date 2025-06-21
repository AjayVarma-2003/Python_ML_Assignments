import sys
import os

def DisplayFiles(DirectoryName, extension):
    Result = []

    flag = os.path.isabs(DirectoryName)
    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)
    if(flag == False):
        print("There is no such directory available.")

    flag = os.path.isdir(DirectoryName)
    if(flag == False):
        print("There is no such directory.")

    for FolderNames, SubFolders, FileName in os.walk(DirectoryName):
        for File in FileName:
            fname = os.path.join(FolderNames, File)
            if(fname.endswith(extension)):
                Result.append(File)

    return Result

def main():
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This is help section.")
            print("Type --u for getting the help for use of the script.")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("This is the use section.")
            print("Type following command to run the script ")
            print("python script.py directoyname extension")

    elif(len(sys.argv) == 3):
        ret = DisplayFiles(sys.argv[1], sys.argv[2])
        print("Files with given extension in the given directory is : ")
        for i in ret:
            print(i)
    else:
        print("Invalid numbers of arguments.")
        print("Type --h for help section.")
        print("Type --u for use section.")

if __name__ == "__main__":
    main()