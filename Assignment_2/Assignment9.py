# Problem Statement - Write a program which accept number from user and return number of digits in that number
# Input : 5187934    Output : 7

def CountDigits(num):
    result = 0
    
    while num > 0:
        num = num // 10    # I googled this as i didn't know how iterate on integers. 
                           # it is floor division operator and returns quotient as output. eg :- 587934 // 10 = 58793
        result = result + 1
        
    return result

def main():
    print("Enter any number : ")
    no = int(input())
    
    ret = CountDigits(no)
    
    print("Number of digits are : ",ret)

if __name__ == "__main__":
    main()