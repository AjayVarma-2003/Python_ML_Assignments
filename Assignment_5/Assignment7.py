# Problem Statement - Accept the length and width of a rectangle. Calculate and display area and perimeter.

def Area(A, B):
    return A * B

def Perimeter(A, B):
    return 2 * (A + B)

def main():
    print("Enter length : ")
    length = int(input())
    
    print("Enter width : ")
    width = int(input())
    
    result = Area(length, width)
    print("Area : ",result)
    
    result = Perimeter(length, width)
    print("Perimeter : ",result)

if __name__ == "__main__":
    main()