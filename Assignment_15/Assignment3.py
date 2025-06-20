def CreateFileAndCopyData(Filename):
    fobj = open(Filename, "w")

    print("Enter the data in file : ")
    data = input()
    fobj.write(data + "\n")
    fobj.close()

    fobj = open(Filename, "r")
    data1 = fobj.read()
    print(f"Data in {Filename} is : ", data1)
    fobj.close()

    fobj = open("Demo.txt", "a")
    fobj.write(data1 + "\n")
    fobj.close()

    fobj = open("Demo.txt", "r")
    data = fobj.read()
    print("Data in Demo.txt is : ", data)

def main():
    print("Enter the name of file you want to create : ")
    FileName = input()

    CreateFileAndCopyData(FileName)

if __name__ == "__main__":
    main()