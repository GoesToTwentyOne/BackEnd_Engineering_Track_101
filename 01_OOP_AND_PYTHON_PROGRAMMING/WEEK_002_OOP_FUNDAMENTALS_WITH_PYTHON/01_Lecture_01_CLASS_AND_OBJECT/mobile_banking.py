class Mobile_Banking:
    def __init__(self,balance) -> None:
        self.balance=balance
        self.min_balance=500
        self.max_cashout=25000
    def current_balance(self):
        return self.balance
    def CashIn(self,ammount):
        if ammount>0 and ammount>= self.min_balance:
            self.balance+=ammount
            print(f"You try to cash out {ammount}, which is accept our cashin policy.After cash in {ammount}, your current balance is {self.current_balance()}")
    def CashOut(self,amount):
        if amount>0 and amount>self.max_cashout:
            print(f"You try to cash In {amount}, which is inefficient our cashout policy.You max cashout {self.max_cashout}")
        elif amount>0 and amount<=self.min_balance:
            print(f"You try to cash out {amount}, which is inefficient our cashout policy.You min cashout {self.min_balance}")
        else:
            self.balance-=amount
            print(f"You try to cash out {amount}, which is accept our cashout policy.After cash out {amount}, your current balance is {self.current_balance()}")




Bkash=Mobile_Banking(18000) 
Bkash.CashIn(50000)
Bkash.CashOut(100)
Bkash.CashOut(3000)
        