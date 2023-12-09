class Bank:
    def __init__(self,account_holder_name,branch,intial_balance) -> None:
        self.account_holder_name=account_holder_name #pulic
        self._branch=branch #protected
        self.__intial_balance=intial_balance #private
    
    def getbalence(self):
        return self.__intial_balance
    
    def deposite(self,amount):
        self.__intial_balance+=amount
    def __withdraw_hiden(self,amount):
        if amount< self.__intial_balance:
            self.__intial_balance-=amount
            return self.__intial_balance
    def withdraw(self,amount):
        return self.__withdraw_hiden(amount)


nihadgo75=Bank("Md.Nihad Hossain",'Dhaka',15000)
print(nihadgo75.account_holder_name)
#print(nihadgo75.__intial_balance)
print(nihadgo75.getbalence())
print(nihadgo75.withdraw(500))
print(dir(nihadgo75))
