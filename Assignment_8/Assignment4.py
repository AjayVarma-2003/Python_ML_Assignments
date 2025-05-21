# Problem Statement - Create three threads as small, capital and digits. All threads accept string as parameter. Small thread display number
#                     small characters, capital thread display number of capital characters and digits thread display number of digits. Display
#                     id and name of each thread.

import threading

def getSmallCharacters(value):
    print("Thread id of small is : ",threading.get_ident())
    
    sum = 0
    
    for i in value:
        if i.islower():    # I searched for this method on google and predicted methods for other ones.
          sum = sum + 1
          
    print("Number of small characters is string is : ",sum)  

def getCapitalCharacters(value):
    print("Thread id of capital is : ",threading.get_ident())
    
    sum = 0
    
    for i in value:
        if i.isupper():
            sum = sum + 1
    
    print("Number of capital letters in string is : ",sum)

def getDigits(value):
    print("Thread id of digits is : ",threading.get_ident())
    
    sum = 0
    
    for i in value:
        if i.isdigit():
            sum = sum + 1
            
    print("Number of digits in string is : ",sum)

def main():
    print("Enter any string : ")
    string = input()
    
    small = threading.Thread(target = getSmallCharacters, args = (string, ))
    capital = threading.Thread(target = getCapitalCharacters, args = (string, ))
    digits = threading.Thread(target = getDigits, args = (string, ))
    
    small.start()
    capital.start()
    digits.start()
    
    small.join()
    capital.join()
    digits.join()

if __name__ == "__main__":
    main()