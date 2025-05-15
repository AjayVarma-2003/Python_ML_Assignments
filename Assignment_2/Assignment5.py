# Problems Statement - Write a program which accepts one number from user and check whether number is prime or not.

def ChckPrime(num):
    half_range = int((num / 2) + 1)
    
    if num <= 1:
        return False
    else:
        for i in range(2, half_range):
            if i % num == 0:
                return False
            else:
                return True

def main():
    print("Enter the number : ")
    no = int(input())
    
    ret = ChckPrime(no)
    
    if(ret == True):
        print("It is prime number.")
    else:
        print("It is not a prime number.")

if __name__ == "__main__":
    main()