def main():
    Count = 0

    print("Enter the file name : ")
    FileName = input()

    fobj = open(FileName, "r")
    data = fobj.readlines()

    for i in data:
        list1 = i.split(" ")
        if(len(list1) > 5):
            print(i)

if __name__ == "__main__":
    main()