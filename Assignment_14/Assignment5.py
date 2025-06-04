class BankAccount:
    def __init__(self, A, B, C):
        self.account_number = A
        self.name = B
        self.balance = C
        
    def display(self):
        print("Account number is : ", self.account_number)
        print("Account holder name is : ", self.name)
        print("Account balance is : ", self.balance)
        
    def Deposit(self, Damount):
        self.balance += Damount
        print("Account balance is : ", self.balance)
        
    def Withdraw(self, Wamount):
        self.balance -= Wamount
        print("Account balance is : ", self.balance)

def main():
    print("Enter account number : ")
    acc_number = int(input())
    
    print("Enter account holder name : ")
    name = input()
    
    print("Enter account balance : ")
    balance = int(input())
    
    obj = BankAccount(acc_number, name, balance)
    
    obj.display()
    
    print("Enter deposit amount : ")
    desposit = int(input())
    
    obj.Deposit(desposit)
    
    print("Enter withdraw amount : ")
    withdraw = int(input())
    
    obj.Withdraw(withdraw)

if __name__ == "__main__":
    main()