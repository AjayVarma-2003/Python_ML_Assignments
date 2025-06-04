# I have modified this code so that user can do further different operations with result till they want.

class Calculator:
    def __init__(self, A, B):
        self.no1 = A
        self.no2 = B
        
    def Addition(self):
        result = 0
        result = self.no1 + self.no2
        return result
    
    def Substraction(self):
        result = 0
        result = self.no1 - self.no2
        return result
    
    def Multiplication(self):
        result = 0
        result = self.no1 * self.no2
        return result
    
    def Division(self):
        result = 0.0
        result = self.no1 / self.no2
        return result

print("Enter first number : ")
value1 = int(input())

def main():
    global value1
    
    print("Enter second number : ")
    value2 = int(input())
    
    obj = Calculator(value1, value2)
    
    print("Enter operation you want to perform : ")
    operation = input().lower()
    
    if(operation == "+"):
        ret = obj.Addition()
        print("Addition of numbers is : ", ret)
    elif(operation == "-"):
        ret = obj.Substraction()
        print("Substraction of numbers is : ", ret)
    elif(operation == "*"):
        ret = obj.Multiplication()
        print("Multiplication of numbers is : ", ret)
    elif(operation == "/"):
        ret = obj.Division()
        print("Division of numbers is : ", ret)
    else:
        return
    
    print("Want to continue (yes/no) :")
    user = input()
    if(user == "yes"):
        value1 = ret
        main()
    else:
        return

if __name__ == "__main__":
    main()