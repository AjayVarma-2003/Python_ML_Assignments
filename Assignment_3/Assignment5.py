# Problem statement - Write a program which accepts N numbers from user and store it in list. Return addition of all 
#                     prime numbers from that list. Main python file accepts N numbers from user and pass each number
#                     to ChckPrime() function which is part of our user-defined module named as MarvellousNum. Name the
#                     function from main python file should be listprime().
# Input : Number of elements = 11
#         Input elements = 13 5 45 7 4 56 10 34 2 5 8
# Output : 54 (13 + 5 + 7 + 2 + 5)

from MarvellousNum import ChckPrime

def listprime(task, values):
    result = []
    
    for i in values:
        ret = task(i)
        
        if ret == True:
            result.append(i)
            
    return result

def Sum(values):
    result = 0
    
    for i in values:
        result = result + i
        
    return result

def main():
    print("Enter number of elements : ")
    size = int(input())
    
    data = []
    for i in range(size):
        no = int(input())
        data.append(no)
        
    new_list = listprime(ChckPrime, data)
    
    ans = Sum(new_list)
    print("Addition of all prime numbers of list is : ",ans)

if __name__ == "__main__":
    main()