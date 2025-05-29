class Numbers:
    def __init__(self, no):
        self.No = no
        
    def ChckPrime(self):
        divisors = 0
        
        if(self.No <= 1):
            return False
        else:
            for i in range(1, self.No+1):
                if(self.No % i == 0):
                    divisors += 1
        
        if(divisors > 2):
            return False
        else:
            return True
    
    def ChckPerfect(self):
        sum = 0
        
        for i in range(1, self.No):
            if(self.No % i == 0):
                sum += i
                
        if(sum == self.No):
            return True
    
    def Factors(self):
        Fact = []
        
        for i in range(1, self.No+1):
            if(self.No % i == 0):
                Fact.append(i)
                
        return Fact
    
    def SumFactors(self):
        sum = 0
        
        for i in range(1, self.No+1):
            if(self.No % i == 0):
                sum += i
                
        return sum

def main():
    print("Enter the number : ")
    value = int(input())
    
    Obj1 = Numbers(value)
    ret = Obj1.ChckPrime()
    if(ret == True):
        print("The number is prime number.")
    else:
        print("The number is not a prime number.")
        
    Obj2 = Numbers(value)
    ret = Obj2.ChckPerfect()
    if(ret == True):
        print("The number is perfect number.")
    else:
        print("The number is not a perfect number.")
        
    Obj3 = Numbers(value)
    ret = Obj3.Factors()
    print("The factors of number is : ",ret)
    
    Obj4 = Numbers(value)
    ret = Obj4.SumFactors()
    print("The sum of factors of number is : ",ret)

if __name__ == "__main__":
    main()