class SimpleBank:
    def __init__(self,initial_balance):
        self.balance = initial_balance
        self.min_deposite=100
        self.max_deposite=4500000
    def get_balance(self):
        return f"your current balance {self.balance}"
    def deposite(self,balance):
        if balance > self.min_deposite:
            self.balance += balance
            print(f"After deposite {balance} your current balance is {self.balance}")
        else:
            print(f" Your balance is too low {balance}")
    def withdraw(self,balance):
        if balance <= self.max_deposite and balance <= self.balance:
            self.balance -= balance
            print(f"Your balance withdaraw requesst {balance}.Successfully withdraw {balance} .Now current balance is {self.balance}")
        else:
            print(f" Your balance is not correct {balance}")

SonaliBank=SimpleBank(5000)
print(SonaliBank.get_balance())
SonaliBank.deposite(4000)
SonaliBank.withdraw(1000)
SonaliBank.withdraw(10000)

TrustBank=SimpleBank(15000)
print(TrustBank.get_balance())
TrustBank.deposite(14000)
TrustBank.withdraw(10000)
TrustBank.withdraw(700000)