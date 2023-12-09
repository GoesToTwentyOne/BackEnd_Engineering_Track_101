class Bank:
    def __init__(self,init_balance):
        self.init_balance=init_balance
        self.min_withdraw=100
        self.max_withdraw=50000
    def getBalance(self):
        return self.init_balance
    def deposite(self,amount):
        self.init_balance+=amount
        print(f'you deposite : {amount}')
    def withdraw(self,amount):
        if amount<self.min_withdraw:
            print(f"Your limit must be will be {self.min_withdraw} your request is not applicaple,because you excist min limit {amount}")
        elif amount>self.max_withdraw:
            print(f"Your limit must be will be {self.max_withdraw} your request is not applicaple,because you excist max limit {amount}")
        else:
            self.init_balance-=amount
            print(f"after withdraw {amount},your balance is {self.getBalance()}")

brac = Bank(25000)
brac.deposite(2500)
print(brac.getBalance())
brac.withdraw(50)
brac.withdraw(78000000)
brac.withdraw(4500)
print(brac.getBalance())


Sonali = Bank(27000)
Sonali.deposite(2700)
print(Sonali.getBalance())
Sonali.withdraw(50)
Sonali.withdraw(7000000)
Sonali.withdraw(500)
print(Sonali.getBalance())