import os
import sys

def CompareData(Filename1, Filename2):
    fobj1 = open(Filename1, "r")
    fobj2 = open(Filename2, "r")

    data = fobj1.read()
    data1 = fobj2.read()

    if(data == data1):
        return "Success"
    else:
        return "Failure"

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

    elif(len(sys.argv) == 3):
        ret = CompareData(sys.argv[1], sys.argv[2])
        print("Data of both files are same or not : ", ret)
            
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