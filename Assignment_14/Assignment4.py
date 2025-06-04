class Student:
    school_name = ""
    
    def __init__(self, A, B):
        self.name = A
        self.roll_no = B
        
    def DisplayStudentInfo(self, sName):
        Student.school_name += sName
        print("Name of student is : ", self.name)
        print("Roll number of student is : ", self.roll_no)
        print("School name of student is : ", Student.school_name)

def main():
    print("Enter the name of student : ")
    name = input()
    
    print("Enter roll number of student : ")
    roll = int(input())
    
    print("Enter name of school of student : ")
    school_name = input()
    
    obj = Student(name, roll)
    
    obj.DisplayStudentInfo(school_name)

if __name__ == "__main__":
    main()