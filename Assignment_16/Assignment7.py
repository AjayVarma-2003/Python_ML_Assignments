def FilterFile(Filename):
    Result = []

    fobj = open(Filename, "r")
    data = fobj.readlines()

    for i in data:
        list1 = i.split(" ")
        if(int(list1[3]) >= 75):
            Result.append(i)

    return Result

def CreateFile(Filename, Size):
    fobj = open(Filename, "w")

    print("Enter the data of students : ")

    for i in range(Size):
        print("Enter name of Student (Name Sirname): ")
        name = input()
        fobj.write(name + " = ")

        print("Enter the marks of Student : ")
        marks = int(input())
        fobj.write(str(marks))
        fobj.write(" "+"\n")

    fobj.close()
    
    result = FilterFile(Filename)

    return result

def main():
    print("Enter the name of file to create : ")
    FileName = input()

    print("Enter the number of students : ")
    size = int(input())

    ret = CreateFile(FileName, size)
    print("Students with more than 75 marks are : ")
    for i in ret:
        print(i)

if __name__ == "__main__":
    main()