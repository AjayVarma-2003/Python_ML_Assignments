# Problem Statement - Write a recursive function to calculate x^n.

sum = 1

def Calculate(num, power):
    global sum
    
    if(power > 0):
        sum = sum * num
        power = power - 1
        Calculate(num, power)
        
    return sum

def main():
    print("Enter number : ")
    no = int(input())
    
    print("Enter power : ")
    power = int(input())
    
    result = Calculate(no, power)
    print("Value is : ",result)
    
if __name__ == "__main__":
    main()