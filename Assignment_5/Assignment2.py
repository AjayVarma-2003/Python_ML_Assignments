# Problem Statement - Accept a single character from user and check if it is a vowel(a, e, i, o, u). If not,
#                     print it's a consonant.

def ChckVowel(A):
    if((A == 'a') or (A == 'e') or (A == 'i') or (A == 'o') or (A == 'u')):
        return True
    else:
        return False

def main():
    print("Enter character : ")
    char = input()
    
    if(len(char) > 1):
        print("Enter single character only")
        return
    
    ret = ChckVowel(char)
    
    if(ret == True):
        print(char," is vowel.")
    else:
        print(char," is consonant.")

if __name__ == "__main__":
    main()