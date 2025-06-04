class Book:
    def __init__(self, A):
        self.__price = A
        
    def getprice(self):
        print("Price of book is : ", self.__price)
        
    def setPrice(self, nPrice):
        self.__price = nPrice
        print("New changed price of book is : ", self.__price)

def main():
    print("Enter book price : ")
    no = int(input())
    
    obj = Book(no)
    
    obj.getprice()
    
    print("Enter changed price of book : ")
    no1 = int(input())
    
    obj.setPrice(no1)

if __name__ == "__main__":
    main()