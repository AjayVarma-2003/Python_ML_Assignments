class Demo:
    Value = 0
    
    def __init__(self, A, B):
        self.No1 = A
        self.No2 = B
        
    def Fun(self):
        print("First number of Fun : ",self.No1)
        print("Second number of Fun : ",self.No2)
        
    def Gun(self):
        print("First number of Gun : ",self.No1)
        print("Second number of Gun : ",self.No2)

def main():
    print("Enter first number : ")
    value1 = int(input())
    
    print("Enter Second number : ")
    value2 = int(input())
    
    obj = Demo(value1, value2)
    obj1 = Demo(11, 21)
    obj2 = Demo(51, 101)
    
    obj.Fun()
    obj.Gun()
    
    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()

if __name__ == "__main__":
    main()