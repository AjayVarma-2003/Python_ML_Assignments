import sys
import os
import shutil

def CopyFiles(Directory1, Directory2, Extension):

    if not os.path.exists(Directory2):
        os.mkdir(Directory2)

    Directory2 = os.path.abspath(Directory2)

    flag = os.path.isabs(Directory1)
    if(flag == False):
        Directory1 = os.path.abspath(Directory1)

    flag = os.path.exists(Directory1)
    if(flag == False):
        print("Thers is no such directory.")

    flag = os.path.isdir(Directory1)
    if(flag == False):
        print("There is no such directory.")

    for FolderName, SubFolders, FileNames in os.walk(Directory1):
        for File in FileNames:
            fname = os.path.join(FolderName, File)
            if fname.endswith(Extension):
                shutil.copy(fname, Directory2)

def main():
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This is help section.")
            print("Type --u for getting the help for use of the script.")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("This is the use section.")
            print("Type following command to run the script ")
            print("python script.py directoyname extension")

    elif(len(sys.argv) == 4):
        CopyFiles(sys.argv[1], sys.argv[2], sys.argv[3])

    else:
        print("Invalid numbers of arguments.")
        print("Type --h for help section.")
        print("Type --u for use section.")

if __name__ == "__main__":
    main()