class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self.__bank_balance = 500000
        self.__user_balance = 0
        
    def deposit(self, amount):
        if amount > 0:
            self.__bank_balance += amount
            self.__user_balance += amount
            print(f"Deposited ${amount} into your account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__user_balance:
            self.__bank_balance -= amount
            self.__user_balance -= amount
            print(f"Withdrew ${amount} from your account.")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def get_user_balance(self):
        return self.__user_balance

    def get_bank_balance(self):
        return self.__bank_balance
        
# Create a bank instance
sonaliBank = Bank("Sonali Bank")

# Check initial balances
print(sonaliBank.name)
print("User Balance:", sonaliBank.get_user_balance())
print("Bank Balance:", sonaliBank.get_bank_balance())

# Deposit money
sonaliBank.deposit(10000)
print("User Balance after deposit:", sonaliBank.get_user_balance())
print("Bank Balance after deposit:", sonaliBank.get_bank_balance())

# Withdraw money
sonaliBank.withdraw(5000)
print("User Balance after withdrawal:", sonaliBank.get_user_balance())
print("Bank Balance after withdrawal:", sonaliBank.get_bank_balance())

# Attempt to withdraw more than user's balance
sonaliBank.withdraw(10000)
