class Account:
    def __init__(self, account_number, balance):
        self.balance = balance
        self.account_number = account_number

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful!")
        else:
            print("Withdrawal unsuccessful!")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful!")
        else:
            print("Deposit unsuccessful!")

    def get_balance(self):
        return self.balance

    def calculate_interest(self):
        pass

    def __str__(self):
        return f'Account with balance: {str(self.balance)}'
