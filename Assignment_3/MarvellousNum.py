def ChckPrime(num):
    divisors = 0
    
    if num == 2:
        return True
    
    if num <= 1:
        return False
    else:
        for i in range(1, num + 1):
            if(num % i == 0):
                divisors = divisors + 1
            
    if divisors > 2:
        return False
    else:
        return True
    