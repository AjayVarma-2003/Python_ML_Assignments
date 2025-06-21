import os
import sys

def CopyFileContent(Filename):
    flag = os.path.exists(Filename)
    if(flag == False):
        print("There is no such file.")
        exit()

    fobj = open(Filename, "r")
    data = fobj.read()
    fobj.close()

    fobj = open("Demo.txt", "w")
    fobj.write(data)
    fobj.close()

    print("Data of given file successfully copied in Demo.txt file.")

def main():
    Border = "-" * 54

    print(Border)
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This is help section.")
            print("Type --u with command to get the help for use of script.")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("This is use section.")
            print("Type the command like following : ")
            print("python script.py filename")

        else:
            CopyFileContent(sys.argv[1])
            
            print(Border)
            print(Border)

        exit()

    else:
        print("Invalid number of arguments.")
        print("type --h for help section.")
        print("type --u for use section.")

    print(Border)
    print(Border)
 
if __name__ == "__main__":
    main()