# Problem Statement - Accept age from user and check whether the person is eligible to vote. (Age should be 18 or above).

def ChckEligibility(A):
    if(A < 18):
        return False
    else:
        return True

def main():
    print("Enter age : ")
    age = int(input())
    
    ret = ChckEligibility(age)
    
    if(ret == True):
        print("Eligible to vote.")
    else:
        print("Not Eligible to vote.")

if __name__ == "__main__":
    main()