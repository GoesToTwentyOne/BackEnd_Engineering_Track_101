class Bank:
    def __init__(self,balance) -> None:
        self.balance=balance
        self.min_withdraw=100
        self.max_withdraw=5000
    def get_balance(self):
        return self.balance
    
    def deposite(self,amount):
        self.balance+=amount
        x=f'After deposite {amount} total balance is {self.balance}'
        print(x)
    
    def withdraw(self,amount):
        if amount>0 and amount>self.min_withdraw:
            self.balance-=amount
            x=f'After withdraw {amount} total balance is {self.get_balance()}'
            print(x)
        else:
            print("insufficient query")
my_bank=Bank(5000)
my_bank.deposite(4500)
print(my_bank.get_balance())
my_bank.withdraw(500)
print(my_bank.get_balance())

my_bank2=Bank(3000)
my_bank2.deposite(4500)
print(my_bank2.get_balance())
my_bank2.withdraw(500)
print(my_bank2.get_balance())


