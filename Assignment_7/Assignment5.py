# Problem Statement - Write a function that accepts string and checks whether it is pallindrome.

def CheckPallindrome(A):
    pallindrome = ""
    string_len = len(A) - 1
    
    for i in range(string_len, -1, -1):
        pallindrome = pallindrome + A[i]
        
    if(pallindrome == A):
        return True
    else:
        return False

def main():
    print("Enter string : ")
    string = input()
    
    result = CheckPallindrome(string)
    
    if(result == True):
        print(string," is pallindrome.")
    else:
        print(string," is not pallindrome.")

if __name__ == "__main__":
    main()