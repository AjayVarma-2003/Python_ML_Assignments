# Problem Statement - Accept the number from user and check whether it is prime is not

def Chckprime(num):
    divisiors = 0
    
    if(num <= 1):
        return False
    else:
        for i in range(1, num + 1):
            if(num % i == 0):
                divisiors = divisiors + 1
                
    if(divisiors > 2):
        return False
    else:
        return True

def main():
    print("Enter the number : ")
    no = int(input())
    
    ret = Chckprime(no)
    
    if(ret == True):
        print(no," is prime number.")
    else:
        print(no," is not prime number.")
    
if __name__ == "__main__":
    main()