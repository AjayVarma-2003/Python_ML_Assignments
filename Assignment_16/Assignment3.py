def main():
    count = 0
    print("Enter the name of file : ")
    Filename = input()

    fobj = open(Filename, "r")
    
    data = fobj.read()

    for i in data:
        if(i == "\n"):
            count += 1
    print("Total number of lines in file is : ", count)
    count = 0

    list1 = data.split(" ")
    
    for i in list1:
        count += 1
    print("Total number of words in file is : ", count)
    count = 0

    for i in list1:
        for j in i:
            count += 1
    print("Total number of characters in file is : ", count)

if __name__ == "__main__":
    main()