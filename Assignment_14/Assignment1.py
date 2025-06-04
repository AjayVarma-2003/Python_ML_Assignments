class Employee:
    def __init__(self, A, B, C):
        self.name = A
        self.emp_id = B
        self.salary = C
        
    def DisplayInfo(self):
        print("Name of employee : ", self.name)
        print("Employee ID : ", self.emp_id)
        print("Salary : ", self.salary)

def main():
    print("Enter name of employee : ")
    name = input()
    
    print("Enter employee id : ")
    id = int(input())
    
    print("Enter salary of employee : ")
    sal = int(input())
    
    obj = Employee(name, id, sal)
    
    print("Employee information")
    obj.DisplayInfo()

if __name__ == "__main__":
    main()