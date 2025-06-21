import sys

def Check(Filename, string):
    Count = 0

    fobj = open(Filename, "r")
    data = fobj.read()
    
    list1 = data.split()

    for i in list1:
        if(i == string):
            Count += 1

    return Count

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
        ret = Check(sys.argv[1], sys.argv[2])
        print(f"Given string occured {ret} times.")
            
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