def main():
    print("Enter the name of file you want check if any blank lines in that and remove them  : ")
    Filename = input()

    fobj = open(Filename, "r")
    data = fobj.readlines()

    fobj1 = open("new.txt", "w")

    for i in data:
        if i.strip():
            fobj1.write(i)

if __name__ == "__main__":
    main()