# Problem Statement - Accept temperature in Celsius and convert it to Fahrenhiet using formula F = (C * (9 / 5)) + 32

def Fahrenhiet(temperature):
    ans = (temperature * (9 / 5)) + 32
    return ans

def main():
    print("Enter temperature in Celsius : ")
    temp = int(input())
    
    result = Fahrenhiet(temp)
    
    print("Temperature in Fahrenhiet : ",result,"F")

if __name__ == "__main__":
    main()