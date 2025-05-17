# Problem Statement - Write a function that accepts a list of integers and returns a list of prime numbers using filter.

def ChckPrime(num):
    divisors = 0
    
    if(num <= 1):
        return False
    else:
        for i in range(1, num + 1):
            if(num % i == 0):
                divisors = divisors + 1
                
    if(divisors > 2):
        return False
    else:
        return True

def main():
    print("Enter number of elements : ")
    size = int(input())
    
    data = []
    print("Enter numbers : ")
    for i in range(size):
        no = int(input())
        data.append(no)
        
    result = list(filter(ChckPrime, data))
    print("Prime numbers are : ",result)

if __name__ == "__main__":
    main()