# Problem Statement - Write a recursive function to calculate sum from 1 to N natural numbers.

sum = 0

def Sum(num):
    global sum
    
    if(num > 0):
        sum = sum + num
        num = num - 1
        Sum(num)
        
    return sum

def main():
    print("Enter number : ")
    no = int(input())
    
    result = Sum(no)
    print("Addition of all numbers till ",no," is : ",result)

if __name__ == "__main__":
    main()