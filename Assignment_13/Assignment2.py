class BankAccount:
    ROI = 10.5
    
    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount
        
    def Deposit(self, DAmount):
        self.Amount = self.Amount + DAmount
    
    def Withdraw(self, WAmount):
        self.Amount = self.Amount - WAmount
        
    def CalculateInterest(self):
        Interest = 0.0
        Interest = ((self.Amount) * (10.5/100))
        print("Interest on the remaining amount will be : ",Interest)
        self.Amount = self.Amount + Interest
        
    def Display(self):
        print("Name of Bank account is : "+self.Name)
        print("Amount in account is : ",self.Amount)

def main():
    print("Enter name of bank account holder : ")
    value1 = input()
    print("Enter the amount in bank account : ")
    value2 = int(input())
    
    Obj1 = BankAccount(value1, value2)
    Obj1.Display()
    
    print("Enter the amount to deposit: ")
    Deposit_amount = int(input())
    Obj1.Deposit(Deposit_amount)
    print("Amount in bank account is : ",Obj1.Amount)
    
    print("Enter amount to withdraw : ")
    Withdraw_amount = int(input())
    Obj1.Withdraw(Withdraw_amount)
    print("Amount in bank account is : ",Obj1.Amount)
    
    Obj1.CalculateInterest()
    Obj1.Display()

if __name__ == "__main__":
    main()