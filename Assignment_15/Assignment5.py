def Check(Filename, string, Data = ""):
    Count = 0

    if Data:
        fobj = open(Filename, "a")
        fobj.write(Data + "\n")
        fobj.close()

    fobj = open(Filename, "r")
    data = fobj.read()
    
    list1 = data.split()

    for i in list1:
        if(i == "Marvellous"):
            Count += 1

    return Count

def main():
    data = ""    # to avoid unboundlocalerror

    print("Enter the name of file : ")
    Filename = input()

    print("Want to enter the data in file or not (yes/no) : ")
    user = input().lower()
    if(user == "yes"):
        print("Enter the data : ")
        data = input()

    print("Enter the string you want to find how many times it occured in file : ")
    string = input()

    ret = Check(Filename, string, data)
    print(f"{string} occured {ret} times in file.")

if __name__ == "__main__":
    main()