# Problem Statement - Accept the list of numbers and use filter() to keep only even numbers.

def ChckEven(num):
    if(num % 2 == 0):
        return True
    else:
        return False

def main():
    print("Enter number of elements : ")
    size = int(input())
    
    data = []
    print("Enter numbers : ")
    for i in range(size):
        no = int(input())
        data.append(no)
        
    result = list(filter(ChckEven, data))
    print("Even numbers : ",result)

if __name__ == "__main__":
    main()