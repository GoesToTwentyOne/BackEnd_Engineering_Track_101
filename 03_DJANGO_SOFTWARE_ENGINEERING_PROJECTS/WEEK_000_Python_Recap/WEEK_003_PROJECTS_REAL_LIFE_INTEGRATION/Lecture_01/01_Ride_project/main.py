class Bank:
    total_bank_balance = 0
    total_loan_amount = 0
    loan_feature_enabled = True
    user_lst = []
    admin_lst = []

    @staticmethod
    def get_user_lst():
        return Bank.user_lst


class User(Bank):
    def __init__(self, user_name, user_password, account_number, user_balance):
        self.user_name = user_name
        self.user_password = user_password
        self.account_number = account_number
        self.user_balance = user_balance
        self.loan_amount = 0
        self.transaction_history = []

    @classmethod
    def user_create_account(cls, user_name, user_password, initial_deposit):
        account_number = f'2023000{len(cls.get_user_lst()) + 1}'
        new_user = cls(user_name, user_password, account_number, initial_deposit)
        Bank.total_bank_balance += initial_deposit
        cls.user_lst.append(new_user)

    def deposit(self, amount):
        self.user_balance += amount
        Bank.total_bank_balance += amount
        self.transaction_history.append(f"Deposited: {amount}")
        print(f"Successfully Deposited: {amount}")

    def withdraw(self, amount):
        if Bank.total_bank_balance < amount and self.user_balance >= amount:
            print("The bank is bankrupt")
        else:
            if self.user_balance >= amount:
                self.user_balance -= amount
                Bank.total_bank_balance -= amount
                self.transaction_history.append(f"Withdrawn: {amount}")
                print(f"Successfully Withdrawn: {amount}")
            else:
                print("Insufficient balance!")

    def transfer(self, recipient, amount):
        recipient_obj = None
        for user in Bank.get_user_lst():
            if user.user_name == recipient:
                recipient_obj = user
                break
        if recipient_obj:
            if self.user_balance >= amount:
                self.user_balance -= amount
                recipient_obj.user_balance += amount
                self.transaction_history.append(f"Transferred: {amount} to {recipient}")
                print(f"Transferred: {amount} to {recipient}")
                recipient_obj.transaction_history.append(f"Received: {amount} from {self.user_name}")
            else:
                print("Insufficient balance!")
        else:
            print(f"No user found named {recipient}")

    def get_user_balance(self):
        print('Your available Balance:', self.user_balance)

    def take_loan(self):
        if Bank.loan_feature_enabled:
            loan_limit = self.user_balance * 2
            if loan_limit > Bank.total_bank_balance:
                print(f"Bank dosen't have sufficient balance for amount: {loan_limit}")
            else:
                if self.loan_amount < loan_limit:
                    loan_amount = loan_limit - self.loan_amount
                    self.user_balance += loan_amount
                    self.loan_amount += loan_amount
                    self.transaction_history.append(f"Loan Taken: {loan_amount}")
                    Bank.total_loan_amount += loan_amount
                    print(f"Loan Taken Successfully. Amount: {loan_amount}")
                    return loan_amount
                else:
                    print("You have reached the maximum loan limit.")
        else:
            print("The loan feature is currently disabled.")

    def get_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)


class Admin(Bank):
    def __init__(self, admin_name, admin_password):
        self.admin_name = admin_name
        self.admin_password = admin_password

    @classmethod
    def admin_create_account(cls, admin_name, admin_password):
        new_admin = cls(admin_name, admin_password)
        cls.admin_lst.append(new_admin)

    @staticmethod
    def check_bank_balance():
        print('Total Bank Balance:', Bank.total_bank_balance)

    @staticmethod
    def check_loan_amount():
        print('Total Loan given:', Bank.total_loan_amount)

    @staticmethod
    def toggle_loan_feature():
        Bank.loan_feature_enabled = not Bank.loan_feature_enabled
        if Bank.loan_feature_enabled:
            print("Loan feature has been enabled.")
        else:
            print("Loan feature has been disabled.")


def main():
    bank = Bank()
    while True:
        print('---------- Welcome to Our Bank -----------')
        print('What are you? \n1) Admin 2) User 3) Exit')
        user_input = int(input('Enter your choice: '))
        
        if user_input == 3:
            break
        
        elif user_input == 1:
            print('------------ Welcome Admin -------------')
            print("1) Login \n2) Create an account \n3) Exit")
            admin_input = int(input('Enter your choice: '))
            
            if admin_input == 3:
                break
            
            elif admin_input == 2:
                admin_name = input("Enter your name: ")
                admin_password = input("Enter your password: ")
                Admin.admin_create_account(admin_name, admin_password)
                print('Successfully created an admin account. Now please login')
            
            elif admin_input == 1:
                admin_name = input("Enter your name: ")
                admin_password = input("Enter your password: ")
                found_admin = None
                
                for admin in Admin.admin_lst:
                    if admin.admin_name == admin_name and admin.admin_password == admin_password:
                        found_admin = admin
                        break
                
                if found_admin:
                    while True:
                        print("1) Check Total Bank Balance \n2) Check Total Loan Amount \n3) Toggle Loan Feature \n4) Exit")
                        admin_input = int(input('Enter your choice: '))
                        
                        if admin_input == 1:
                            Admin.check_bank_balance()
                            
                        elif admin_input == 2:
                            Admin.check_loan_amount()
                            
                        elif admin_input == 3:
                            Admin.toggle_loan_feature()
                            
                        elif admin_input == 4:
                            break
                else:
                    print('Invalid Admin name and password')
        
        elif user_input == 2:
            print('------------ Welcome User -------------')
            print("1) Login \n2) Create an account \n3) Exit")
            user_input = int(input('Enter your choice: '))
            
            if user_input == 3:
                break
            
            elif user_input == 2:
                user_name = input("Enter your name: ")
                user_password = input("Enter your password: ")
                initial_deposit = int(input("Enter your deposit amount: "))
                User.user_create_account(user_name, user_password, initial_deposit)
                print('Successfully created a user account. Now please login')
            
            elif user_input == 1:
                user_name = input("Enter your name: ")
                user_password = input("Enter your password: ")
                found_user = None
                
                for user in User.user_lst:
                    if user.user_name == user_name and user.user_password == user_password:
                        found_user = user
                        break
                
                if found_user:
                    while True:
                        print("1) Deposit  \n2) Withdraw  \n3) Check Account Balance \n4) Take Loan \n5) Transfer \n6) Transaction History \n7) Exit")
                        user_input = int(input('Enter your choice: '))
                        
                        if user_input == 1:
                            deposit_amount = int(input("Enter your Deposit amount: "))
                            found_user.deposit(deposit_amount)
                            
                        elif user_input == 2:
                            withdraw_amount = int(input("Enter the amount to withdraw: "))
                            found_user.withdraw(withdraw_amount)
                        
                        elif user_input == 3:
                            found_user.get_user_balance()
                        
                        elif user_input == 4:
                            found_user.take_loan()
                        
                        elif user_input == 5:
                            recipient = input('Enter receiver name: ')
                            transfer_amount = int(input("Enter Transfer Amount: "))
                            found_user.transfer(recipient, transfer_amount)
                        
                        elif user_input == 6:
                            found_user.get_transaction_history()
                        
                        elif user_input == 7:
                            break
                else:
                    print('Invalid User name and password')

if __name__ == '__main__':
    main()

   