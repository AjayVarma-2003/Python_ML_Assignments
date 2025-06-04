class Product:
    def __init__(self, value1):
        self.value = value1
        
    def __eq__(self, value2):    # used to compare two values in class
        if isinstance(value2, Product):
            if(self.value == value2.value):
                return True
        return False 

def main():
    obj = Product(100)
    obj1 = Product(101)
    
    print(obj == obj1)

if __name__ == "__main__":
    main()