# Problem Statement - Print the sum of even numbers between 1 to 100. Use loop to find and print the sum
#                     of all even numbers from 1 to 100.

def main():
    result = 0
    
    for i in range(1, 101):
        if(i % 2 == 0):
            result = result + i
            
    print("Sum of even numbers between 1 to 100 is : ",result)

if __name__ == "__main__":
    main()