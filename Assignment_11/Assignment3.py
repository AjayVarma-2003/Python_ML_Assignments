# Problem Statement - Write a recursive function to calculate the sum of digits of number.

sum = 0

def Sum(num):
    global sum
    
    if(num > 0):
        sum = sum + (num % 10)
        num = num//10
        Sum(num)
        
    return sum

def main():
    print("Enter number : ")
    no = int(input())
    
    result = Sum(no)
    print("Addition of digits of numbers is : ",result)

if __name__ == "__main__":
    main()