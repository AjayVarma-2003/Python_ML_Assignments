class Circle:
    PI = 3.14
    
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0
        
    def Accept(self, A):
        self.Radius = A
    
    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius
    
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius
        
    def Display(self):
        print("Radius entered is : ",self.Radius)
        print("Area of Circle is : ",self.Area)
        print("Circumference of Circle is : ",self.Circumference)

def main():
    print("Enter the value of radius : ")
    radius = float(input())
    
    obj = Circle()
    
    obj.Accept(radius)
    obj.CalculateArea()
    obj.CalculateCircumference()
    obj.Display()

if __name__ == "__main__":
    main()