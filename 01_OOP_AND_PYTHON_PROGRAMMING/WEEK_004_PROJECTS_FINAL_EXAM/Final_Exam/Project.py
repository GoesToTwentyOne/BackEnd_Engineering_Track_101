class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class User(Person):
    def __init__(self, name, email, phone):
        super().__init__(name, email, phone)
        self.account_number = None
        self.credit_card = None
        self.pin = None
        self.__balance = 0
        self.role = "user"
        self.transaction_history=[]
        self.total_loan_amount=0

    def deposit_amount(self, amount):
        if amount > 0:
            self.__balance += amount
            x=f"Deposit {amount} is successful"
            self.transaction_history.append(x)
            print(x)
        else:
            print("Sorry for server Issue")
        
    def bankrupt_check(self,amount):
        total_balance = self.balance
        for user in self.customer:
            total_balance += user.available_balance
        if total_balance<amount:
            return False

    def withdraw_amount(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            x=f"Withdraw {amount} is successful"
            self.transaction_history.append(x)
            print(x)
        
        elif self.bankrupt_check(amount)==False:
            print("The bank is bankrupt.")
        else:
            print(f"Please enter the correct amount")
    def userinfo(self):
        print(f"Name {self.name}\nPhone {self.phone}\n Email {self.email}\nAccount Number {self.account_number}\nCredit Card {self.credit_card}\nRole {self.role}")


    @property
    def available_balance(self):
        return self.__balance

    def transfer_amount(self, amount, recipient):
        if self.__balance >= amount:
            self.__balance -= amount
            recipient.deposit_amount(amount)
            x=f"Transfer {amount} is successful to {recipient.name}"
            self.transaction_history.append(x)
            print(x)
        else:
            print(f"Please enter the correct amount to transfer")

    def take_loan(self):
        
            loan_amount = self.__balance * 2
            self.total_loan_amount=loan_amount
            self.__balance += loan_amount
            x=f"Loan {loan_amount} credited succesfully."
            self.transaction_history.append(x)
            print(x)

    def get_transaction_history(self):
        for index, transaction in enumerate(self.transaction_history):
            print(index, transaction)


class Admin(User):
    def __init__(self, name, email, phone):
        super().__init__(name, email, phone)
        self.role = "admin"
        self.admin_id=1

    def total_available_balance_bank(self, bank):
        total_balance = bank.balance
        for user in bank.customer:
            total_balance += user.available_balance
        print("Total available balance in the bank:", total_balance)
    
    def total_loan_balance_bank(self, bank):
        total_loan = bank.total_loan_amount
        for user in bank.customer:
            total_loan += user.total_loan_amount
        print("Total  loan in the bank:", total_loan)
    def admininfo(self):
        print(f"Name {self.name}\nPhone {self.phone}\n Email {self.email}\nAccount Number {self.admin_id}\nRole {self.role}")
    
    def loan_on_off(self, bank, agree):
        bank.loan_features_state = agree
        print("Loan feature is", "enabled" if agree else "disabled")

class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.customer = []
        self.admin = []
        self.loan_features_state=False
        self.total_loan_amount=0


    def create_account_user(self, user, amount):
        user.account_number = 10001 + len(self.customer)
        user.credit_card = len(self.customer)+1
        user.pin = 88880 + len(self.customer)
        user.deposit_amount(amount)
        user.role='user'

    def add_user(self, user, amount):
        if user.role == 'user':
            self.create_account_user(user, amount)
            self.customer.append(user)
        elif user.role == 'admin':
            self.create_account_user(user, amount)
            self.customer.append(user)
        else:
            print("You aren't able to create an account.")

    def create_account_admin(self, user):
        user.admin_id = len(self.admin)
        user.role='admin'


    def add_admin(self, user):
        if user.role == 'admin':
            self.create_account_admin(user)
            self.admin.append(user)
        else:
            print("You aren't able to create an admin.")
    def get_loan_state(self):
        print(self.loan_features_state)

#<-----------------------------------User------------------------------------------->

# Create a bank
bank = Bank("Sonali Bank", 500)

 #user INFO
Nihad = User("Nihad Hossain", "niahdgo75@gmail.com", "8801773684304")
Sakib = User("Sakib", "niahdgo75@gmail.com", "8801773684304")
Tamim = User("Tamim", "niahdgo75@gmail.com", "8801773684304")
Afiif = User("Tamim", "niahdgo75@gmail.com", "8801773684304")

#CREATE CUSTOMER with intial deposite
bank.add_user(Nihad, 5000)
bank.add_user(Sakib, 3000)

#Customer Info
Nihad.userinfo()

#Customer deposit
Nihad.deposit_amount(500)

#Customer current balance
print(Nihad.available_balance)
#Customer withdraw
Nihad.withdraw_amount(500)
#Customer current balance
print(Nihad.available_balance)
#customer tranfer amount
Nihad.transfer_amount(1200,Sakib)
print(Nihad.available_balance)
print(Sakib.available_balance)
#Transaction History
Nihad.get_transaction_history()
#take loan
Nihad.take_loan()
#balance
print(Nihad.available_balance)

#<-----------------------------------Andmin------------------------------------------->
#admin Info
Alex=Admin("Alex","ALex@gmail.com",884454545454)
#create admin
bank.add_admin(Alex)
#admin info print
Alex.userinfo()
#tottal balane in the bank
Alex.total_available_balance_bank(bank)

#total loan amount in the bank
Alex.total_loan_balance_bank(bank)
#loan State
bank.get_loan_state()
#change state
Alex.loan_on_off(bank,True)
#loan State
bank.get_loan_state()
#change state
Alex.loan_on_off(bank, False)














    





















