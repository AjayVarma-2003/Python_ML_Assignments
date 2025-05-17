# Problem Statement - Accept number from the user and print its multiplication table up to 10.

def main():
    print("Enter the number : ")
    no = int(input())
    
    result = 1
    
    for i in range(1, 11):
        result = i * no
        print(no," * ",i," : ",result)

if __name__ == "__main__":
    main()