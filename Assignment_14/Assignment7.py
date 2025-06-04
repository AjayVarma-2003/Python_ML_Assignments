class Person:
    def __init__(self, A, B):
        self.name = A
        self.Age = B
        
    def Display(self):
        print("Name is : ", self.name)
        print("Age is : ", self.Age)
        
class Teacher(Person):
    def __init__(self, name, Age, salary):
        super().__init__(name, Age)
        self.salary = salary
        
    def Display(self):
        super().Display()
        print("Salary is : ", self.salary)

def main():
    print("Enter name : ")
    name = input()
    
    print("Enter age : ")
    age = int(input())
    
    print("Enter salary is : ")
    Salary = int(input())
    
    obj = Teacher(name, age, Salary)
    obj.Display()

if __name__ == "__main__":
    main()