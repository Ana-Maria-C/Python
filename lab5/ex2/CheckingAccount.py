from ex2.Account import Account


class CheckingAccounts(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def calculate_interest(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            return True
        else:
            return False

    def withdraw(self, amount):
        if self.calculate_interest(amount):
            self.balance -= amount
            print("Withdrawal successful!")
        else:
            print("Withdrawal unsuccessful!")

    def __str__(self):
        return f'CheckingAccount with balance: {str(self.balance)} and overdraft limit: {str(self.overdraft_limit)}'
