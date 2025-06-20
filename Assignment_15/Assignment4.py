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
    print("Enter the first file name : ")
    Filename1 = input()

    print("Enter the second file name : ")
    Filename2 = input()

    ret = CompareData(Filename1, Filename2)
    print(ret)

if __name__ == "__main__":
    main()