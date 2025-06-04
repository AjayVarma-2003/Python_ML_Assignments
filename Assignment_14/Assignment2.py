class Rectangle:
    def __init__(self, A, B):
        self.length = A
        self.width = B
        
    def CalculateArea(self):
        result = 0
        result = self.length * self.width
        return result
    
    def CalculatePerimeter(self):
        result = 0
        result = 2 * (self.length + self.width)
        return result

def main():
    print("Enter length of rectangle : ")
    length = int(input())
    
    print("Enter width of rectangle : ")
    width = int(input())
    
    obj = Rectangle(length, width)
    
    ret = obj.CalculateArea()
    print("Area of rectangle is : ", ret)
    
    ret = obj.CalculatePerimeter()
    print("Perimeter of rectangle is : ", ret)

if __name__ == "__main__":
    main()