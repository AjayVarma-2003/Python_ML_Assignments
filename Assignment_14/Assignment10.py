class Employee:
    def __init__(self, A, B, C):
        self.name = A
        self._department = B    # protected
        self.__salary = C       # private
        
    def Display(self):
        print("Name is : ", self.name)
        print("Department is : ", self._department)
        print("Salary is : ", self.__salary)

def main():
    obj = Employee("Ajay", "Computer", 10000)
    
    obj.Display()
    
    print(obj.name)
    print(obj._department)
    # print(obj.__salary)    # it will raise error as it is private accessifier and allowed to use in class only.

if __name__ == "__main__":
    main()