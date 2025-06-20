def main():
    print("Enter name of file : ")
    Filename = input()

    fobj = open(Filename, "a")

    print("Enter the numbers in file : ")
    for i in range(10):
        no = int(input())
        fobj.write(str(no) + "\n")
    
    fobj.close()

    fobj = open(Filename, "r")
    data = fobj.read()
    print("Data of file is : ", data)

if __name__ == "__main__":
    main()