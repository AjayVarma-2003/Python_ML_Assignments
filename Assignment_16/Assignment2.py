def main():
    print("Enter the file to create : ")
    Filename = input()

    fobj = open(Filename, "w")
    print("Enter any data in file : ")
    data = input()
    fobj.write(data)
    fobj.close()

    fobj = open(Filename, "r")
    data = fobj.read()
    print("Data in file is : ", data)
    fobj.close()

if __name__ == "__main__":
    main()