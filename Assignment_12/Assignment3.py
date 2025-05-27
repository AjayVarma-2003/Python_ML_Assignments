class Arithematic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
        
    def Accept(self, A, B):
        self.Value1 = A
        self.Value2 = B
        
    def Addition(self):
        Ans = 0
        Ans = self.Value1 + self.Value2
        return Ans
    
    def Substraction(self):
        Ans = 0
        Ans = self.Value1 - self.Value2
        return Ans
    
    def Multiplication(self):
        Ans = 0
        Ans = self.Value1 * self.Value2
        return Ans
    
    def Division(self):
        Ans = 0
        Ans = self.Value1 / self.Value2
        return Ans

def main():
    print("Enter first number : ")
    no1 = int(input())
    
    print("Enter second number : ")
    no2 = int(input())
    
    obj = Arithematic()
    obj.Accept(no1, no2)
    
    ret = obj.Addition()
    print("Addition of numbers is : ",ret)
    
    ret = obj.Substraction()
    print("Substraction of numbers is : ",ret)
    
    ret = obj.Multiplication()
    print("Multiplication of numbers is : ",ret)
    
    ret = obj.Division()
    print("Division of numbers is : ",ret)

if __name__ == "__main__":
    main()